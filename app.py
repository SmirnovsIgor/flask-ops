from flask import Flask

import string
import secrets

app = Flask(__name__)

# Generate a simple key
def generate():
    rand_device = string.ascii_letters + string.digits
    return ''.join(secrets.choice(rand_device) for i in range(8))

@app.route('/')
def signature():
    return generate()
