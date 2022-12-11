from gudlft_app.tests.utilities import assert_template
from flask import url_for, request


def test_places_must_not_be_empty(app, first_club_test, first_competition_test, second_competition_test, third_competition_test):
    email = first_club_test['email']
    places_required = ""
    assert not places_required
    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        'You have to pick a number.',
        email=email,
        data=dict(places=places_required, club=first_club_test['name'], competition=first_competition_test['name']),
        club=first_club_test,
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )


def test_places_must_be_positive(app, first_club_test, first_competition_test, second_competition_test, third_competition_test):
    email = first_club_test['email']
    places_required = -3
    assert places_required < 0
    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        'You have to pick a positive number of places.',
        email=email,
        data=dict(places=str(places_required), club=first_club_test['name'], competition=first_competition_test['name']),
        club=first_club_test,
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )


def test_places_must_be_less_than_available_points(app, second_club_test, first_competition_test, second_competition_test, third_competition_test):
    email = second_club_test['email']
    places_required = 6
    assert places_required > int(second_club_test['points'])

    points_before_booking = second_club_test['points']
    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {points_before_booking}",
        "You cannot book more places than you have points available for your club.",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=first_competition_test['name']),
        club=second_club_test,
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )
    assert points_before_booking == second_club_test['points']
    assert int(second_club_test['points']) == 4


def test_booking_no_more_than_twelve_places(app, second_club_test, first_competition_test, second_competition_test, third_competition_test):
    email = second_club_test['email']
    places_required = 13
    assert places_required > 12
    points_before_booking = second_club_test['points']

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {points_before_booking}",
        "You cannot book more than 12 places per competition.",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=first_competition_test['name']),
        club=second_club_test,
        competitions=[first_competition_test, second_competition_test, third_competition_test]
    )


def test_booking_with_enough_points(app, second_club_test, first_competition_test, second_competition_test, third_competition_test):
    email = second_club_test['email']
    places_required = 2
    assert places_required <= int(second_club_test['points'])
    points_before_booking = second_club_test['points']

    modified_first_competition_test = first_competition_test
    modified_first_competition_test["number_of_places"] = 13

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {points_before_booking}",
        "Great - booking complete!",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=first_competition_test['name']),
        club=second_club_test,
        competitions=[modified_first_competition_test, second_competition_test, third_competition_test]
    )
