from .zi_api_auth_client import AuthClient


def user_name_pwd_authentication(user_name, password):
    auth_client = AuthClient(user_name)
    return auth_client.user_name_pwd_authentication(password)


def pki_authentication(user_name, client_id, private_key):
    auth_client = AuthClient(user_name)
    return auth_client.pki_authentication(client_id, private_key)