from gudlft_app.server import load_clubs, load_competitions


def test_load_clubs(first_club_test, second_club_test, third_club_test):
    """Tests load_clubs function."""
    clubs = load_clubs('features/clubs_tests.json')
    expected_clubs = [first_club_test, second_club_test, third_club_test]
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


def test_load_competitions(first_competition_test, second_competition_test, third_competition_test):
    """Tests load_competitions function."""
    competitions = load_competitions('features/competitions_tests.json')
    expected_competitions = [first_competition_test, second_competition_test, third_competition_test]
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
