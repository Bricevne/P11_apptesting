from flask import template_rendered, url_for, request, json
from contextlib import contextmanager


@contextmanager
def captured_templates(app):
    """Context manager recording a specific template to test."""

    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def validate_template(app, url, template_name, *args):
    """Function validating a template."""
    with app.test_client() as client:
        with captured_templates(app) as templates:
            response = client.get(url)
            template, context = templates[0]
            assert template.name == template_name
            assert len(templates) == 1
            html = response.data.decode()
            # All html texts
            for data in args:
                assert data in html


def test_index_should_status_code_ok(client):
    """Tests if index status code is 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_index_template_is_valid(app):
    """Tests if the template accessed by the '/' url is the index.html template."""
    validate_template(
        app,
        '/',
        'index.html',
        "Welcome to the GUDLFT Registration Portal!",
        "Please enter your secretary email to continue:",
        "Email:",
        "Enter"
    )


def test_index_wrong_email_address(client):
    """Tests if the index template displays the corresponding message when a wrong email address is entered."""
    email = "wrong.email@gmail.com"
    response = client.post('/show-summary', data={'email': email}, follow_redirects=True)
    html = response.data.decode()
    assert "The email address wrong.email@gmail.com does not exist. Please try again." in html


def test_index_no_email_address(client):
    """Tests if the index template displays the corresponding message when no email address is entered."""
    email = ""
    response = client.post('/show-summary', data={'email': email}, follow_redirects=True)
    html = response.data.decode()
    assert "You have to enter an email address. Please try again." in html


def test_logout(app):
    """Tests if the '/logout' url redirects to the index."""
    with app.test_client() as client:
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        # Check that the second request was to the index page.
        assert request.path == url_for('index')




