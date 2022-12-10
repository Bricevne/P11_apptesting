from gudlft_app.tests.utilities import assert_template


def test_show_summary_get_method_with_session(
        app, first_club_test, first_competition_test, second_competition_test, third_competition_test
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
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )


def test_show_summary_post_method(
        app, first_club_test, first_competition_test, second_competition_test, third_competition_test
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
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )
