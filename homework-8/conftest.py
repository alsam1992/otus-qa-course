"""Module with fixtures for tests"""
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        required=True,
    )

    parser.addoption(
        "--browser",
        action="store",
        required=True,
    )


@pytest.fixture
def get_driver(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser.lower() == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser.lower() == 'safari':
        driver = webdriver.Safari()
    else:
        raise ValueError('--browser option can have chrome or firefox value')
    request.addfinalizer(driver.quit)

    driver.get(url)
    return driver
