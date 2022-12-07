import json
from flask import Flask, render_template, request, redirect, flash, url_for, session

CLUBS = 'clubs.json'
CLUBS_TESTS = 'features/clubs_tests.json'


# def load_clubs():
#     with open('clubs.json') as c:
#         list_of_clubs = json.load(c)['clubs']
#         return list_of_clubs

def load_clubs(file: str):
    with open(file) as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


def create_app(config):
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config["TESTING"] = config.get("TESTING")

    if app.config["TESTING"]:
        competitions = load_competitions()
        clubs = load_clubs(CLUBS_TESTS)
    else:
        competitions = load_competitions()
        clubs = load_clubs(CLUBS)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/show-summary', methods=['GET', 'POST'])
    def show_summary():

        # Fix bug 1: No management of wrong email address.
        email = request.form['email']
        try:
            club = [club for club in clubs if club['email'] == email][0]
        except IndexError:
            if not email:
                flash("You have to enter an email address. Please try again.")
            else:
                flash(f"The email address {email} does not exist. Please try again.")
            return redirect(url_for('index'))

        return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [c for c in competitions if c['name'] == competition][0]
        if found_club and found_competition:
            return render_template('booking.html', club=found_club, competition=found_competition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/purchase-places', methods=['POST'])
    def purchase_places():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        places_required = int(request.form['places'])
        competition['number_of_places'] = int(competition['number_of_places']) - places_required
        flash('Great - booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # TODO: Add route for points display

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app


app = create_app({"TESTING": False})

if __name__ == "__main__":
    app.run()
