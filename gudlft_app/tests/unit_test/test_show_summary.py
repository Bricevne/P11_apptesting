from gudlft_app.tests.utilities import assert_template
from flask import url_for, request


def test_show_summary_wrong_email_address(client):
    """Tests if the index template displays the corresponding message when a wrong email address is entered."""
    email = "wrong.email@gmail.com"
    response = client.post('/show-summary', data={'email': email}, follow_redirects=True)
    html = response.data.decode()
    assert "The email address wrong.email@gmail.com does not exist. Please try again." in html


def test_show_summary_no_email_address(client):
    """Tests if the index template displays the corresponding message when no email address is entered."""
    email = ""
    response = client.post('/show-summary', data={'email': email}, follow_redirects=True)
    html = response.data.decode()
    assert "You have to enter an email address. Please try again." in html


def test_no_access_to_show_summary_without_login(app):
    """Tests if show_summary with a 'GET' method without being logged in redirects to index."""
    with app.test_client() as client:
        response = client.get('/show-summary', follow_redirects=True)
        assert request.path == url_for('index')
        assert response.status_code == 200


def test_show_summary_get_method_with_session(
        app, first_club_test, second_competition_test, fourth_competition_test
):
    # ADD pytest.fixture maybe for individual clubs and competitions.
    """Tests if the Welcome.html template is valid when a user is already logged in.
     '/show-summary' with 'GET' method."""
    email = first_club_test["email"]
    assert_template(
        app,
        "GET",
        True,
        "/show-summary",
        "welcome.html",
        200,
        email=email,
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_show_summary_post_method(
        app, first_club_test, second_competition_test, fourth_competition_test
):
    """Tests if the Welcome.html template while not logged in.
     '/show-summary' with 'POST' method."""

    email = first_club_test["email"]
    assert_template(
        app,
        "POST",
        False,
        "/show-summary",
        "welcome.html",
        200,
        data=dict(email=email),
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )
