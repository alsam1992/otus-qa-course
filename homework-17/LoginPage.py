"""Module contains Page-object classes"""


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
