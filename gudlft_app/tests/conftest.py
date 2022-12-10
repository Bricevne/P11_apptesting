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


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        return client


@pytest.fixture
def first_club_test():
    return {
        "name": "Test 1",
        "email": "test1@gmail.com",
        "points": "13"
    }


@pytest.fixture
def second_club_test():
    return {
        "name": "Test 2",
        "email": "test2@gmail.com",
        "points": "4"
    }


@pytest.fixture
def third_club_test():
    return {
        "name": "Test 3",
        "email": "test3@gmail.com",
        "points": "12"
    }


@pytest.fixture
def first_competition_test():
    return {
        "name": "Competition test 1",
        "date": "2020-05-27 12:00:00",
        "number_of_places": "15"
    }


@pytest.fixture
def second_competition_test():
    return {
        "name": "Competition test 2",
        "date": "2023-05-22 13:30:00",
        "number_of_places": "19"
    }


@pytest.fixture
def third_competition_test():
    return {
        "name": "Competition test 3",
        "date": "2021-03-25 10:00:00",
        "number_of_places": "10"
    }
