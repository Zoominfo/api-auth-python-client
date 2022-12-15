"""
This file supports 2 types of authentication methods:
1. Username and password authentication
2. PKI authentication
"""

import jwt
from datetime import datetime, timedelta
import requests
import json


class AuthClient:
    def __init__(self, user_name):
        self.user_name = user_name
        self.audience = 'enterprise_api'
        self.issuer = 'api-client@zoominfo.com'
        self.authenticate_url = "https://api.zoominfo.com/authenticate"
        self.expiry_time_in_seconds = 300
        self.hashing_algorithm = 'RS256'

    def user_name_pwd_authentication(self, password):
        headers = {'Accept': "application/json", 'user-agent': ""}
        request_body = {'username': self.user_name, 'password': password}
        response = requests.post(self.authenticate_url, headers=headers, data=request_body)
        if not response.ok:
            response.reason = response.text
            return response.raise_for_status()
        return self._extract_jwt_from_text(response.text)

    def pki_authentication(self, client_id, private_key):
        return self._post_and_get_jwt(client_id, private_key)

    def _post_and_get_jwt(self, client_id, private_key):
        client_jwt = self._get_client_jwt(client_id, private_key)
        headers = {'Authorization': f"Bearer {client_jwt}", 'Accept': "application/json", 'user-agent': ""}
        response = requests.post(self.authenticate_url, headers=headers)
        if not response.ok:
            response.reason = response.text
            return response.raise_for_status()
        return self._extract_jwt_from_text(response.text)

    def _get_client_jwt(self, client_id, private_key):
        current_time = datetime.utcnow()
        claims = {
            'aud': self.audience,
            'iss': self.issuer,
            'iat': current_time,
            'exp': current_time + timedelta(seconds=self.expiry_time_in_seconds),
            'client_id': client_id,
            'username': self.user_name
        }
        encoded_jwt = jwt.encode(claims, private_key, algorithm=self.hashing_algorithm)
        # `PyJWT` switched to returning a string in v2.0.0
        return encoded_jwt.decode("utf-8") if isinstance(encoded_jwt, bytes) else encoded_jwt

    def _extract_jwt_from_text(self, text_input):
        json_response = json.loads(text_input)
        return json_response["jwt"]
