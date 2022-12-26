# Improve a Python Web Application with tests and debugging - OpenClassrooms project 11

This project is about debugging and implementing new functionalities to an existing Flask project

## Project structure

The root is composed of :

a requirements.txt file listing all the necessary packages for this project

a .gitignore file

a gudlft_app containing:

- a config.py file with the configuration parameters of this application
- clubs.json and competitions.json files with the data for clubs and competitions of the application
- a server.py file with the different views executed on the different URLs
- a features package composed of two json files (clubs_test.json and competitions_test.json) used as a database when testing the app
- a template package with all HTML files
- a .coveragerc file with the configuration for the tests coverage of the web application
- a htmlcov package with all reports of the coverage
- a tests package with:
  - a conftest.py file for all tests fixtures
  - a utilities.py for functions used if several test files
  - functional, integration and unit tests packages
  - a performance_tests package with a unique locustfile to evaluate the performance of the application

## Workflow of the project

This project if organized in 12 branches of which 6 are dedicated to fixing bugs and improvement, and 1 to a new feature:

- 01_improvement/fix-naming-conventions-pocoo-styleguide
- 02_improvement/refacto-template-language
- 03_bug/entering-an-unknown-email-crashes-the-app
- 04_bug/clubs-should-not-be-able-to-use-more-than-their-points-allowed
- 05_bug/clubs-should-not-be-allowed-to-book-more-than-12-places-per-competition
- 06_bug/point-updates-are-not-reflected
- 07_bug/booking-places-in-past-competitions
- 08_improvement/cannot-access-booking-without-being-logged-in
- 09_feature/implement-points-display-board
- QA :the quality audit branch
- develop : an intermediate branch between main and the rest of the branches, permitting to modify the main branch only after the whole project is finished
- main : the principal branch

For this project, the main branch is at its initial state. The develop branch has all modifications (bug fixes and new feature).
The QA branch has all necessary updates for a clean code (Docstrings, requirements, etc.)

## Installation

Clone [the repository](https://github.com/Bricevne/P11_apptesting.git) on your computer.

```
git clone https://github.com/Bricevne/P11_apptesting.git
```

Get into the root directory P11_apptesting/

Set your virtual environment under [python 3.10](https://www.python.org/downloads/release/python-3100/)

<code>virtualenv .</code>

```bash
virtualenv . # Create the virtual environment
source bin/activate # Activate the virtual environment
pip install -r requirements.txt # Install the dependencies
```

Flask requires that you set an environmental variable to the python file. You'll want to set the file to be <code>server.py</code>. 

Get into the gudlft_app directory and export the server.py as a FLASK_APP parameter

```bash
export FLASK_APP=server.py  
```

Go to the QA branch to get the final version of the project:

```bash
git checkout QA
```

## Launch the local server

In the gudlft_app folder run the following code to access the api:

```bash
flask run # Start the local server
```

You can now open your navigator with the URL 'http://127.0.0.1:5000/' and login to the web app with one of the emails in the clubs.json file

## Testing

Pytest is used to perform the testing of the whole flask application.

### Unit, integration and functional tests

You can launch unit, integration and functional tests individually by running the command <code>pytest tests/folder</code>

```bash
pytest tests/unit_tests/ # For unit tests
pytest tests/integration_tests/ # For integration tests
pytest tests/functional_tests/ # For functional tests
```

You can lauch all tests by running:

```bash
pytest
```

### Coverage

To obtain coverage of the tests, you can run:

```bash
pytest --cov=.
```

To obtain the full html report:

```bash
 pytest --cov=. --cov-report html
 ```

### Performance tests

To access performance tests, get into the gudlft_app/tests/performance_tests/ folder and run the following command:

```bash
locust
```

Once you’ve started Locust, open up a browser and point it to http://localhost:8089. 
You can then insert the number of users, the spawn rate and the host (respectively 6, 1 and http://127.0.0.1:5000 for
this specific testing), and access the different tabs.

## License

[MIT](https://choosealicense.com/licenses/mit/)