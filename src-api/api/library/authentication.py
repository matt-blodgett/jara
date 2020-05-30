import datetime

import jwt

from rest_framework import exceptions
from rest_framework import authentication

from jara.settings import SECRET_KEY


class TokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()

        if not auth or len(auth) != 2 or auth[0].lower() != b'token':
            msg = 'Invalid token: Token string should be in the form of "Token {token_value}"'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token: UnicodeError'
            raise exceptions.AuthenticationFailed(msg)

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.DecodeError:
            msg = 'Invalid token: DecodeError'
            raise exceptions.AuthenticationFailed(msg)

        expiry = payload.get('expiry', None)

        if not expiry:
            msg = 'Invalid token: No expiry in claims'
            raise exceptions.AuthenticationFailed(msg)

        if expiry < datetime.datetime.now().timestamp():
            msg = 'Invalid token: Token is expired'
            raise exceptions.AuthenticationFailed(msg)

        return payload, token

    def authenticate_header(self, request):
        return 'Token'
