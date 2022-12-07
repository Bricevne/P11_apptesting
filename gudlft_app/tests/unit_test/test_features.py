from flask import template_rendered, url_for, request

from gudlft_app.server import load_clubs


def test_load_clubs(client):
    """Tests load_clubs function."""
    clubs = load_clubs('features/clubs_tests.json')
    expected_clubs = [
        {
            "name": "Test 1",
            "email": "test1@gmail.com",
            "points": "13"
        },
        {
            "name": "Test 2",
            "email": "test2@gmail.com",
            "points": "4"
        },
        {
            "name": "Test 3",
            "email": "test3@gmail.com",
            "points": "12"
        }
    ]
    assert clubs == expected_clubs
