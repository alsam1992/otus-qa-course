"""Module with testsuite of tests for JSON API tests"""


class BasePage(object):
    """Base page class"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def navigate(self):
        """Public method to page navigate"""
        self.driver.get(self.url)
        self.driver.maximize_window()


class LoginPage(BasePage):
    """Login page class"""

    def _get_title_(self):
        return self.driver.title

    def get_title(self):
        """public method to get page title"""
        return self._get_title_()


class TestSuite:
    """Testsuite for base page tests"""

    def test_is_base_page(self, get_driver, cmdopt_url):
        """test for is base page"""
        login_page = LoginPage(get_driver, cmdopt_url)
        login_page.navigate()
        assert "Your Store" in login_page.get_title()
