from contextlib import contextmanager
from flask import template_rendered


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


def assert_template(app, method, logged_in, url, template_name, status_code, *args, email="", data=None, **kwargs):
    """Function validating a template."""
    with captured_templates(app) as templates:
        with app.test_client() as client:
            if logged_in:
                with client.session_transaction() as session:
                    session['email'] = email
                    assert 'email' in session
            if method == "POST":
                response = client.post(url, data=data)
            else:
                response = client.get(url)
            template, context = templates[0]
            assert template.name == template_name
            assert len(templates) == 1
            assert response.status_code == status_code
            html = response.data.decode()
            # All html texts
            for data in args:
                assert data in html
            # All context
            for key, value in kwargs.items():
                assert context[key] == value
