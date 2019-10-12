"""Module contains class with locators"""
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for login page locators"""
    INPUT_USERNAME = (By.ID, 'input-username')
    INPUT_PASSWORD = (By.ID, 'input-password')
    BUTTON_LOGIN = (By.XPATH, "//button[@class='btn btn-primary'][@type='submit']")
    ALERT = (By.XPATH, "//div[@class='alert alert-danger']")

