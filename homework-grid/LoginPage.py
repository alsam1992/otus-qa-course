"""Module contains Page-object classes"""
from locators import MainPageLocators


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

    def _get_alert_(self):
        return self.driver.find_element(*MainPageLocators.ALERT).text

    def _set_username_(self, username):
        self.driver.find_element(*MainPageLocators.INPUT_USERNAME).send_keys(username)

    def _set_password_(self, password):
        self.driver.find_element(*MainPageLocators.INPUT_PASSWORD).send_keys(password)

    def _click_login_button_(self):
        self.driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()

    def get_title(self):
        """public method to get page title"""
        return self._get_title_()

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_()

    def login(self, username, password):
        """public method to login"""
        self._set_username_(username)
        self._set_password_(password)
        self._click_login_button_()




