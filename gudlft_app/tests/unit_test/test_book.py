from flask import request, url_for

from gudlft_app.tests.utilities import assert_template


def test_cannot_access_booking_if_not_logged_in(app, first_club_test, second_competition_test):
    assert_template(
        app,
        "GET",
        False,
        url_for('book', competition=second_competition_test['name'], club=first_club_test['name']),
        "index.html",
        200,
    )


def test_cannot_access_booking_of_other_clubs(app, first_club_test, second_club_test, second_competition_test, fourth_competition_test):
    email = first_club_test["email"]
    assert_template(
        app,
        "GET",
        True,
        url_for('book', competition=second_competition_test['name'], club=second_club_test['name']),
        "welcome.html",
        200,
        "You cannot access booking for another club - please try again.",
        email=email,
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_cannot_access_booking_with_wrong_competition_name(app, first_club_test, second_competition_test, fourth_competition_test):
    email = first_club_test["email"]
    assert_template(
        app,
        "GET",
        True,
        url_for('book', competition="New%20Competition", club=first_club_test['name']),
        "welcome.html",
        200,
        "Something went wrong - please try again.",
        email=email,
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_access_booking(app, first_club_test, second_competition_test, fourth_competition_test):
    email = first_club_test["email"]
    assert_template(
        app,
        "GET",
        True,
        url_for('book', competition=second_competition_test['name'], club=first_club_test['name']),
        "booking.html",
        200,
        f"{second_competition_test['name']}",
        f"Places available: {second_competition_test['number_of_places']}",
        email=email,
        club=first_club_test,
        competition=second_competition_test
    )
