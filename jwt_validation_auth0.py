import json
from urllib.request import urlopen

from jose import jwt

AUTH0_DOMAIN = 'huffer.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'p3auth'
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpBZ0hYUUNlZ2NCVEdySUoza1F6ciJ9.eyJpc3MiOiJodHRwczovL2h1ZmZlci5ldS5hdXRoMC5jb20vIiwic3ViIjoiaXY1MmhjWkFYNnhIbEI0Z1dGdEVBTlc5Rm5mWGVHUHhAY2xpZW50cyIsImF1ZCI6InAzYXV0aCIsImlhdCI6MTY1NzY1MjA0MiwiZXhwIjoxNjU3NzM4NDQyLCJhenAiOiJpdjUyaGNaQVg2eEhsQjRnV0Z0RUFOVzlGbmZYZUdQeCIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.hBdFx8iB1AsYD0snPqpZtViJKKd-E7-jcnC5JlXci32baxhuZhKQJrQ9p8gdtPDf0d8RfwJltXpjqJTenfv7fMN1KrHWHkv379Sd63XyRUAHlBXbXsDLtECEKufA9sQLN7ywK1xS7ZDvqSwj82LOY9Xgkwzcu_IPyuECGeC04yqj88I57hgcDPVRAzCcy_IiEg6gc58JDXDXiM9pPX9Qx7JaCndIO4T8LkEntfhvf4r6aKCy9QxMJHdkNymq_e2Ukv9jWPwOOwinJVmxc0gNBJF971zGBQPqjz9WguZ3XQPYM95JtBXSbW5PmjCX47xFyVcjlKfnrur10DuzS99Ppw'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


## Auth Header
def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        print('RSA_KEY')
        print(rsa_key)
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


def main():
    verify_decode_jwt(TOKEN)


if __name__ == '__main__':
    main()
