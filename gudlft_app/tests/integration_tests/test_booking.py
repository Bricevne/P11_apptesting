def test_display_new_points_after_booking(client, first_club_test, fourth_competition_test):
    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 10" not in response.data.decode()

    places_required = 3
    data = dict(places=places_required, club=first_club_test['name'], competition=fourth_competition_test['name'])
    client.post("/purchase-places", data=data)

    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 10" in response.data.decode()
    assert "Points available: 13" not in response.data.decode()


def test_display_points_after_booking_more_points_than_available_competition(client, first_club_test, fourth_competition_test):
    """More places asked than available in the competition."""
    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 9" not in response.data.decode()

    places_required = 4
    data = dict(places=places_required, club=first_club_test['name'], competition=fourth_competition_test['name'])
    client.post("/purchase-places", data=data)

    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 9" not in response.data.decode()


def test_display_points_after_booking_more_than_twelve_points(client, first_club_test, second_competition_test):
    """More places asked than available in the competition."""
    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 0" not in response.data.decode()

    places_required = 13
    data = dict(places=places_required, club=first_club_test['name'], competition=second_competition_test['name'])
    client.post("/purchase-places", data=data)

    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 0" not in response.data.decode()


def test_display_points_after_booking_negative_points(client, first_club_test, second_competition_test):
    """More places asked than available in the competition."""
    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 15" not in response.data.decode()

    places_required = -2
    data = dict(places=places_required, club=first_club_test['name'], competition=second_competition_test['name'])
    client.post("/purchase-places", data=data)

    response = client.get("/display-board")
    assert f"{first_club_test['name']}" and "Points available: 13" in response.data.decode()
    assert "Points available: 15" not in response.data.decode()