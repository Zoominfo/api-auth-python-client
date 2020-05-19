"""
This library supports 2 types of authentication methods:
1. Username and password authentication:
   Usage:
          1. auth_client = AuthClient("<user_name>")
          2. jwt_token = auth_client.user_name_pwd_authentication("<password>") // returns the JWT token
2. PKI authentication: This type of authentication needs a private key and a client ID to generate the JWT.
   Usage:
          1. auth_client = AuthClient("<user_name>")
          2. key = '''
                -----BEGIN PRIVATE KEY-----
                <Your private key goes here>
                -----END PRIVATE KEY-----'''
          3. jwt_token = auth_client.pki_authentication("<client_id>", key) // returns the JWT token

Note: If you get the error "ValueError: Could not deserialize key data." when doing PKI authentication, make sure that
your private key is properly formatted. Paste the private key as a multi-line string in python.

Correct way: The following is the right way to paste your private key.
'''
-----BEGIN PRIVATE KEY-----
<Your private key goes here>
-----END PRIVATE KEY-----'''

Wrong way: Pasting the private key as follows would throw the error "ValueError: Could not deserialize key data." because
there are extra spaces on each line in the key.
'''
                -----BEGIN PRIVATE KEY-----
                <Your private key goes here>
                -----END PRIVATE KEY-----'''

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
        headers = {'Accept': "application/json"}
        request_body = {'username': self.user_name, 'password': password}
        response = requests.post(self.authenticate_url, headers=headers, data=request_body)
        if not response.ok:
            raise RuntimeError(response.text)
        return self._extract_jwt_from_text(response.text)

    def pki_authentication(self, client_id, private_key):
        return self._post_and_get_jwt(client_id, private_key)

    def _post_and_get_jwt(self, client_id, private_key):
        client_jwt = self._get_client_jwt(client_id, private_key)
        headers = {'Authorization': f"Bearer {client_jwt}", 'Accept': "application/json"}
        response = requests.post(self.authenticate_url, headers=headers)
        if not response.ok:
            raise RuntimeError(response.text)
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
        return encoded_jwt.decode("utf-8")

    def _extract_jwt_from_text(self, text_input):
        json_response = json.loads(text_input)
        return json_response["jwt"]
