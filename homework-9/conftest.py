"""Module with fixtures for tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options
from pages import LoginPage
from pages import AdminPage
from pages import ProductPage


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="ie", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://127.0.0.1/opencart/admin/", help="url option"
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


@pytest.fixture()
def product_dataset():
    """fixture for storage product data"""
    product_name = 'Phone_1'
    product_meta_tag_title = 'Phone_1'
    product_model = 'Phone_1'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture()
def product_dataset_more():
    """fixture for storage product data"""
    product_name = 'Phone_2'
    product_meta_tag_title = 'Phone_2'
    product_model = 'Phone_2'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture
def login(add_waits, cmdopt_url, login_param):
    """fixture to login"""
    login_page = LoginPage(add_waits, cmdopt_url)
    login_page.navigate()
    login, password = login_param
    login_page.login(login, password)
    login_page.close_modal_window()
    return login_page.get_url()


@pytest.fixture
def login_negative(get_driver, cmdopt_url):
    """fixture to test negative scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("admin", "admin1")
    current_result = login_page.get_alert()
    expected_result = "No match for Username and/or Password."
    return expected_result, current_result


@pytest.fixture
def go_to_product_page(add_waits, login):
    """fixture to add product test"""
    admin_page = AdminPage(add_waits, login)
    admin_page.navigate()
    admin_page.close_modal_window()
    admin_page.choose_catalog()
    admin_page.choose_product()
    return admin_page.get_url()


@pytest.fixture
def add_product(add_waits, go_to_product_page, product_dataset):
    """fixture to add product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def modify_product(add_waits, go_to_product_page, product_dataset_more):
    """fixture to modify product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.modify_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def delete_product(add_waits, go_to_product_page, product_dataset_more):
    """fixture to delete product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.delete_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result
