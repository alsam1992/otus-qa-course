"""Module with fixtures for tests"""
import os
import pkg_resources
import pytest
from selenium import webdriver
from LoginPage import LoginPage


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="firefox", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://demo23.opencart.pro/admin", help="url option"
    )


@pytest.fixture
def cmdopt_browser(request):
    """browser type option"""
    return request.config.getoption("--browser_type")


@pytest.fixture
def cmdopt_url(request):
    """url options"""
    return request.config.getoption("--url")


@pytest.mark.usefixtures("configure_html_report_env")
@pytest.fixture
def get_driver(request, cmdopt_browser):
    """Fixture to create, return and close driver"""
    driver = None
    if cmdopt_browser == "ie":
        driver = webdriver.Ie()
    elif cmdopt_browser == "firefox":
        driver = webdriver.Firefox()
    elif cmdopt_browser == "chrome":
        driver = webdriver.Chrome()
    else:
        return "unsupported browser"

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.mark.usefixtures("environment_info", "packages_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info, packages_info):
    """Fixture for adding environment_info&packages_info"""
    for key, value in environment_info.items():
        request.config._metadata.update(
            {key: value})
    request.config._metadata.update({"installed_packages_list": packages_info})
    yield


@pytest.fixture(scope="session")
def environment_info():
    """Fixture for environment_info"""
    environment_params = {}
    for a in os.environ:
        environment_params.update({a: os.getenv(a)})
    return environment_params


@pytest.fixture(scope="session")
def packages_info():
    """Fixture for packages_info"""
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    return installed_packages_list


@pytest.fixture
def login_positive(get_driver, cmdopt_url):
    """fixture to test positive scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("demo", "demo")
    current_result = login_page.get_title()
    expected_result = "Панель состояния"
    return expected_result, current_result


@pytest.fixture
def login_negative(get_driver, cmdopt_url):
    """fixture to test negative scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("demo", "demon1")
    current_result = login_page.get_alert()
    expected_result = "Такой логин и/или пароль не существует!"
    return expected_result, current_result


@pytest.fixture
def empty_form(get_driver, cmdopt_url):
    """fixture to empty login form scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("", "")
    current_result = login_page.get_alert()
    expected_result = "Такой логин и/или пароль не существует!"
    return expected_result, current_result
