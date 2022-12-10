from gudlft_app.tests.utilities import assert_template


def test_index_should_status_code_ok(client):
    """Tests if index status code is 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_index_template_is_valid(app):
    """Tests if the template accessed by the '/' url is the index.html template."""
    assert_template(
        app,
        "GET",
        False,
        "/",
        "index.html",
        200,
        "Welcome to the GUDLFT Registration Portal!",
        "Please enter your secretary email to continue:",
        "Email:",
        "Enter"
    )

