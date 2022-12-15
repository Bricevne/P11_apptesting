from flask import url_for, request


def test_logout(app):
    """Tests if the '/logout' url redirects to the index and clear the email in the session."""

    email = "test1@gmail.com"
    with app.test_client() as client:
        with client.session_transaction() as session:
            session['email'] = email
            assert 'email' in session

        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        # Check that the second request was to the index page.
        assert response.request.path == url_for('index')
        with client.session_transaction() as session:
            assert 'email' not in session
