import pytest
from flask import Flask

from app import generate


@pytest.fixture()
def app():
    app = Flask(__name__)

    test_salt = "124325246546379565"

    @app.route('/')
    def signature():
        return generate(test_salt)
    return app


@pytest.fixture()
def request_qty():
    return 1

@pytest.fixture
def client(app):
    return app.test_client()
