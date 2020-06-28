import os

import pytest
from flask import Flask

from app import generate


@pytest.fixture()
def app():
    app = Flask(__name__)

    test_salt = os.environ.get('TEST_SALT')

    @app.route('/')
    def signature():
        return generate(test_salt)
    return app


@pytest.fixture
def client(app):
    return app.test_client()
