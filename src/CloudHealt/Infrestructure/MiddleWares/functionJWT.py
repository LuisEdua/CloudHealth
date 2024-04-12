from datetime import timedelta, datetime

from flask import jsonify
from jwt import encode, decode, exceptions
from os import getenv

def expire_date(days: int):
    return datetime.now() + timedelta(days=days)

def write_token(data: dict):
    try:
        secret_key = getenv("SECRET")
        if not secret_key:
            raise ValueError("SECRET environment variable is not set.")
        token = encode(payload={**data, "exp": expire_date(2)}, key=secret_key, algorithm='HS256')
        return token
    except Exception as e:
        return f"Error encoding token: {str(e)}"

def validate_token(token: str, output=False):
    try:
        if output:
            return decode(token, getenv("SECRET"), algorithms=['HS256'])
        decode(token, getenv("SECRET"), algorithms=['HS256'])
    except exceptions.DecodeError:
        response = jsonify({'error': 'Invalid token'})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({'error': 'Token has expired'})
        response.status_code = 401
        return response

