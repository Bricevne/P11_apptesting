import pytest

from gudlft_app.server import create_app


@pytest.fixture
def app():
    return create_app({"TESTING": True})


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        return client
