import jwt

SECRET = 'learning'
ALGORITHM = 'HS256'


def encode(payload):
    return jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)


def decode(encoded_jwt):
    return jwt.decode(jwt=encoded_jwt, key=SECRET, algorithms=[ALGORITHM],
                      verify=True)


def main():
    payload_to_encode = {
        'user_id': 'hehe123',
        'role': 'admin'
    }
    encoded_jwt = encode(payload_to_encode)
    print(encoded_jwt)
    decoded_jwt = decode(encoded_jwt)
    print(decoded_jwt)


def task1():
    jwt_1 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiY2VudHJhbCBwYXJrIn0.H7sytXDEHK1fOyOYkII5aFfzEZqGIro0Erw_84jZuGc'
    # jwt_2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiYmF0dGVyeSBwYXJrIn0.bQEjsBRGfhKKEFtGhh83sTsMSXgSstFA_P8g2qV5Sns'
    print(decode(jwt_1))
    # print(decode(jwt_2))


def task2():
    jwt_1 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiY2VudHJhbCBwYXJrIn0.H7sytXDEHK1fOyOYkII5aFfzEZqGIro0Erw_84jZuGc'
    jwt_2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoidW5pb24gc3F1YXJlIn0.N3EaAHsrJ9-ls82LT8JoFTNpDK3wcm5a79vYkSn8AFY'
    jwt_3 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiYmF0dGVyeSBwYXJrIn0.S3TWkRAiGHZfJA-MYSNKB7fCdstpyaOdXMU6M8dvv7o'
    print(decode(jwt_1))
    print(decode(jwt_2))
    print(decode(jwt_3))


def task3():
    print(encode({'school': 'udacity'}))


if __name__ == '__main__':
    task3()
