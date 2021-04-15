import base64
import binascii
import hashlib
import os

import jwt

def StringToBase64(string):
    message = string.encode("utf-8")
    base64_bytes = base64.b64encode(message)
    return base64_bytes.decode("utf-8")

def Base64ToString(b64):
    base64_bytes = b64.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('utf-8')


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512',
        password.encode('utf-8'),
        salt,
        100000
    )
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512',
        provided_password.encode('utf-8'),
        salt.encode('ascii'),
        100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def jwt_sign(payload, algo="HS512", secret=os.environ["APP_SECRET"]):
    """
        payload of type dict.
        HS512
    """
    return jwt.encode(payload, secret, algorithm=algo)

def jwt_decode(token, algo="HS512", secret=os.environ["APP_SECRET"]):
    """
        payload of type dict.
        HS512
    """
    try:
        payload = jwt.decode(token, secret, algorithms=[algo])
    except jwt.exceptions.InvalidTokenError as e:
        print(e)
        payload = False
    return payload
