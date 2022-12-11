from gudlft_app.tests.utilities import assert_template


def test_places_must_not_be_empty(app, first_club_test, second_competition_test, fourth_competition_test):
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
        f"Points available: {first_club_test['points']}",
        'You have to pick a number.',
        email=email,
        data=dict(places=places_required, club=first_club_test['name'], competition=second_competition_test['name']),
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_places_must_be_positive(app, first_club_test, second_competition_test, fourth_competition_test):
    email = first_club_test['email']
    places_required = -3
    assert places_required <= 0
    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {first_club_test['points']}",
        'You have to pick a positive number of places.',
        email=email,
        data=dict(places=str(places_required), club=first_club_test['name'], competition=second_competition_test['name']),
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_places_must_be_less_than_available_points(app, second_club_test, second_competition_test, fourth_competition_test):
    email = second_club_test['email']
    places_required = 6
    assert places_required
    assert places_required <= 12
    assert places_required > int(second_club_test['points'])

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {second_club_test['points']}",
        "You cannot book more places than you have points available for your club.",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=second_competition_test['name']),
        club=second_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_booking_no_more_than_twelve_places(app, second_club_test, second_competition_test, fourth_competition_test):
    email = second_club_test['email']
    places_required = 13
    assert places_required
    assert places_required > 0
    assert places_required > 12

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {second_club_test['points']}",
        "You cannot book more than 12 places per competition.",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=second_competition_test['name']),
        club=second_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_booking_no_more_than_places_available_in_competition(app, first_club_test, second_competition_test, fourth_competition_test):
    email = first_club_test['email']
    places_required = 12
    assert places_required
    assert places_required > 0
    assert places_required <= 12
    assert places_required <= int(first_club_test["points"])
    assert places_required > int(fourth_competition_test["number_of_places"])

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {first_club_test['points']}",
        "There are not enough places for this competition.",
        email=email,
        data=dict(places=str(places_required), club=first_club_test['name'], competition=fourth_competition_test['name']),
        club=first_club_test,
        competitions=[fourth_competition_test, second_competition_test]
    )


def test_booking_with_enough_points(app, second_club_test, second_competition_test, fourth_competition_test):
    email = second_club_test['email']
    places_required = 2

    assert places_required
    assert places_required > 0
    assert places_required <= 12
    assert places_required <= int(second_club_test["points"])
    assert places_required <= int(fourth_competition_test['number_of_places'])

    modified_second_club_test = second_club_test
    modified_second_club_test["points"] = int(second_club_test['points']) - places_required

    modified_fourth_competition_test = fourth_competition_test
    modified_fourth_competition_test["number_of_places"] = int(fourth_competition_test['number_of_places']) - places_required

    assert_template(
        app,
        "POST",
        True,
        "/purchase-places",
        "welcome.html",
        200,
        f"Points available: {modified_second_club_test['points']}",
        "Great - booking complete!",
        email=email,
        data=dict(places=str(places_required), club=second_club_test['name'], competition=fourth_competition_test['name']),
        club=modified_second_club_test,
        competitions=[modified_fourth_competition_test, second_competition_test]
    )
