from gudlft_app.tests.utilities import assert_template


def test_display_board_not_logged_in(app, first_club_test, second_club_test, third_club_test):
    assert_template(
        app,
        "GET",
        False,
        "/display-board",
        "board.html",
        200,
        f"{first_club_test['name']}",
        f"Points available: {first_club_test['points']}",
        f"{second_club_test['name']}",
        f"Points available: {second_club_test['points']}",
        f"{third_club_test['name']}",
        f"Points available: {third_club_test['points']}",
    )


def test_display_board_logged_in(app, first_club_test, second_club_test, third_club_test):
    assert_template(
        app,
        "GET",
        True,
        "/display-board",
        "board.html",
        200,
        "Welcome, here is the list of all clubs || GUDLFT",
        f"{first_club_test['name']}",
        f"Points available: {first_club_test['points']}",
        f"{second_club_test['name']}",
        f"Points available: {second_club_test['points']}",
        f"{third_club_test['name']}",
        f"Points available: {third_club_test['points']}",
        email=first_club_test['email']
    )
