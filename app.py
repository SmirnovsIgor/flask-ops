"""
### ACME CORP
### Customer session key generator. Protects PII.
### / 2020
"""
import hashlib
import os
import secrets
import string

from flask import Flask

app = Flask(__name__)

SUPER_SECRET_SALT = os.environ.get('SALT')


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def generate(salt):
    rand_device = string.ascii_letters + string.digits
    return encrypt_string((''.join(secrets.choice(rand_device) for i in range(8))).join(salt))


@app.route('/')
def signature():
    return generate(SUPER_SECRET_SALT)
