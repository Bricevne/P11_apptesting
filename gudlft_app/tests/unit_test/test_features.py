from gudlft_app.server import load_clubs, load_competitions


def test_load_clubs():
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


def test_length_clubs_list():
    """Tests length of club list."""
    clubs = load_clubs('features/clubs_tests.json')
    assert len(clubs) == 3
    assert type(clubs) is list


def test_wrong_club_list():
    """Tests load_clubs with wrong list."""
    clubs = load_clubs('features/clubs_tests.json')
    expected_clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]
    assert clubs != expected_clubs


def test_load_competitions():
    """Tests load_competitions function."""
    competitions = load_competitions('features/competitions_tests.json')
    expected_competitions = [
        {
            "name": "Competition test 1",
            "date": "2020-05-27 12:00:00",
            "number_of_places": "15"
        },
        {
            "name": "Competition test 2",
            "date": "2023-05-22 13:30:00",
            "number_of_places": "19"
        },
        {
            "name": "Competition test 3",
            "date": "2021-03-25 10:00:00",
            "number_of_places": "10"
        }
    ]
    assert competitions == expected_competitions


def test_length_competitions_list():
    """Tests length of competition list."""
    competitions = load_competitions('features/competitions_tests.json')
    assert len(competitions) == 3
    assert type(competitions) is list


def test_wrong_competition_list():
    """Tests load_competitions with wrong list."""
    competitions = load_competitions('features/competitions_tests.json')
    expected_competitions = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]
    assert competitions != expected_competitions
