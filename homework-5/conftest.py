"""Module with fixtures for tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="edge", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://127.0.0.1/opencart", help="url option"
    )
    parser.addoption(
        "--window_option", action="store", default="window", help="window option"
    )


@pytest.fixture
def cmdopt_browser(request):
    """browser type option"""
    return request.config.getoption("--browser_type")


@pytest.fixture
def cmdopt_url(request):
    """url options"""
    return request.config.getoption("--url")


@pytest.fixture
def cmdopt_window(request):
    """window option"""
    return request.config.getoption("--window_option")


@pytest.fixture
def get_driver(request, cmdopt_browser, cmdopt_window):
    """Fixture to create, return and close driver"""
    driver = None
    if cmdopt_browser == "ie":
        driver = webdriver.Ie()
    elif cmdopt_browser == "firefox":
        if cmdopt_window == "headless":
            options = Firefox_options()
            options.add_argument("--headless")
            driver = webdriver.Firefox(firefox_options=options)
        else:
            driver = webdriver.Firefox()
    elif cmdopt_browser == "chrome":
        if cmdopt_window == "headless":
            options = Chrome_options()
            options.headless = True
            driver = webdriver.Chrome(chrome_options=options)
        else:
            driver = webdriver.Chrome()
    elif cmdopt_browser == "edge":
        driver = webdriver.Edge()
    else:
        return "unsupported browser"

    def close_driver():
        driver.close()

    request.addfinalizer(close_driver)
    return driver
