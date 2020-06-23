### ACME CORP
### Customer session key generator. Protects PII.
### / 2020

from flask import Flask

import string
import secrets
import hashlib

app = Flask(__name__)


# !! DON'T EXPOSE THIS KEY !!
super_secret_salt = "68874260280172957479"

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# Generate a simple key
def generate():
    rand_device = string.ascii_letters + string.digits
    return encrypt_string((''.join(secrets.choice(rand_device) for i in range(8))).join(super_secret_salt))

@app.route('/')
def signature():
    return generate()
