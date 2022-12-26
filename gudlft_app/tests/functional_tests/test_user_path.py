import multiprocessing

from selenium import webdriver
from flask_testing import LiveServerTestCase
from selenium.webdriver.common.by import By

from gudlft_app.server import create_app

URL = "http://127.0.0.1:5000"


def create_driver():
    """Creates a Chrome driver."""
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    return webdriver.Chrome(options=option)


class UserPath(LiveServerTestCase):
    """Class testing a user path on the web app."""
    multiprocessing.set_start_method("fork")

    def create_app(self):
        """Create_app method necessary when inheriting from LiveServerTestCase."""
        return create_app({"TESTING": True})

    def setUp(self) -> None:
        """Method run before every other method of this class."""
        self.driver = create_driver()

    def tearDown(self) -> None:
        """Method run after every other method of this class."""
        self.driver.close()

    def test_user_logs_in_book_and_check_points(self):
        """Tests if a club can log in, book enough places for a competition, check the display board, and log out."""
        email = "test1@gmail.com"
        self.driver.get(URL)
        assert "Welcome to the GUDLFT Registration Portal" in self.driver.page_source
        self.driver.find_element("id", "email").send_keys(email)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        assert "test1@gmail.com" in self.driver.page_source
        assert "Points available: 13" in self.driver.page_source

        self.driver.find_element(By.LINK_TEXT, 'Display clubs board').click()
        assert "Test 1" in self.driver.page_source
        assert "Points available: 13" in self.driver.page_source
        assert "Points available: 10" not in self.driver.page_source

        self.driver.find_element(By.LINK_TEXT, 'Back').click()

        self.driver.find_element(By.LINK_TEXT, 'Book Places').click()
        self.driver.find_element("name", "places").send_keys("3")
        self.driver.find_element(By.TAG_NAME, 'button').click()
        assert "test1@gmail.com" in self.driver.page_source
        assert "Points available: 10" in self.driver.page_source

        self.driver.find_element(By.LINK_TEXT, 'Display clubs board').click()
        assert "Test 1" in self.driver.page_source
        assert "Points available: 10" in self.driver.page_source
        assert "Points available: 13" not in self.driver.page_source

        self.driver.find_element(By.LINK_TEXT, 'Back').click()

        self.driver.find_element(By.LINK_TEXT, 'Logout').click()

        assert "Welcome to the GUDLFT Registration Portal" in self.driver.page_source
