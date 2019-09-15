"""Module with fixtures for tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options
from pages import LoginPage
from pages import DownloadsPage


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="chrome", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://127.0.0.1/opencart/admin", help="url option"
    )
    parser.addoption(
        "--window_option", action="store", default="window", help="window option"
    )
    parser.addoption(
        "--waits", action="store", default="no_wait", help="wait option"
    )
    parser.addoption(
        "--wait_time", action="store", default=10, help="wait time option"
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
def cmdopt_waits(request):
    """wait option"""
    return request.config.getoption("--waits")


@pytest.fixture
def cmdopt_wait_time(request):
    """wait time option"""
    return request.config.getoption("--wait_time")


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
    else:
        return "unsupported browser"

    def close_driver():
        driver.close()

    request.addfinalizer(close_driver)
    return driver


@pytest.fixture
def add_waits(get_driver, cmdopt_wait_time):
    """fixture for add waits"""
    driver = get_driver
    if cmdopt_waits == "waits":
        driver.implicitly_wait(cmdopt_wait_time)
    else:
        pass
    return driver


@pytest.fixture
def login_param():
    """fixture for storage login&password"""
    login = "admin"
    password = "admin"
    return login, password


@pytest.fixture
def picture_params():
    """fixture for storage description&mask"""
    description = 'new_1'
    mask = 'new_1'
    return description, mask


@pytest.fixture
def login(add_waits, cmdopt_url, login_param):
    """fixture to login"""
    login_page = LoginPage(add_waits, cmdopt_url)
    login_page.navigate()
    login, password = login_param
    login_page.login(login, password)
    return login_page.get_url()


@pytest.fixture
def add_picture(add_waits, login, picture_params):
    """fixture to add picture test for download page"""
    download_page = DownloadsPage(add_waits, login)
    download_page.navigate()
    description, mask = picture_params
    download_page.add_picture(description, mask)
    current_result = download_page.get_file_alert()
    expected_result = "Success: You have modified downloads!"
    return expected_result, current_result
