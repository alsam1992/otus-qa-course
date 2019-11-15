"""Module contains class with locators"""
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for login page locators"""
    INPUT_USERNAME = (By.XPATH, "//input[@id='input-username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='input-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@class='btn btn-primary'][@type='submit']")
    ALERT = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    CLOSE_MODAL_WINDOW = (By.XPATH, "//button[@class='close']")


class AdminPageLocators(object):
    """A class for admin page locators"""
    CLOSE_MODAL_WINDOW = (By.XPATH, "//button[@class='close']")
    CATALOG = (By.XPATH, "//a[@class='parent collapsed']")
    CATALOG_ELEMENTS = (By.TAG_NAME, 'li')


class ProductPageLocators(object):
    """A class for product page locators"""
    BUTTON_ADD_PRODUCT = (By.XPATH, "//a[@class='btn btn-primary']")
    BUTTON_COPY_PRODUCT = (By.XPATH, "//button[@class='btn btn-default']")
    BUTTON_DELETE_PRODUCT = (By.XPATH, "//button[@class='btn btn-danger']")
    TAB_NAVIGATION_PRODUCT = (By.TAG_NAME, 'li')
    INPUT_PRODUCT_NAME = (By.ID, 'input-name1')
    INPUT_PRODUCT_META_TAG_TITLE = (By.ID, 'input-meta-title1')
    INPUT_PRODUCT_MODEL = (By.ID, 'input-model')
    BUTTON_SAVE_PRODUCT = (By.XPATH, "//button[@class='btn btn-primary']")
    ALERT_MODIFY_PRODUCT = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    CHECKBOX_PRODUCT = (By.XPATH, "//td[contains(text(), 'Phone_2')]//..//td/input[@name='selected[]']")
    BUTTON_MODIFY_PRODUCT = (By.XPATH, "//td[contains(text(), 'Phone_2')]//..//td/a[@class='btn btn-primary']")
