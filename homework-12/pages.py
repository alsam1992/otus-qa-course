"""Module contains Page-object classes"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from locators import AdminPageLocators
from locators import ProductPageLocators


class BasePage(object):
    """Base page class"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def _wait_element_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _get_title_(self):
        return self.driver.title

    def _click_close_modal_window_button_(self):
        self._wait_element_(*MainPageLocators.CLOSE_MODAL_WINDOW).click()

    def _get_url_(self):
        return self.driver.current_url

    def get_title(self):
        """public method to get page title"""
        return self._get_title_()

    def navigate(self):
        """Public method to page navigate"""
        self.driver.get(self.url)
        self.driver.maximize_window()

    def close_modal_window(self):
        """public method to close modal window"""
        self._click_close_modal_window_button_()

    def get_url(self):
        """public method to get window url"""
        return self._get_url_()


class LoginPage(BasePage):
    """Login page class"""

    def _get_alert_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.alert_is_present())
            element = self.driver.find_element(by, value)
            return element.text
        except NoAlertPresentException as err:
            raise err

    def _set_username_(self, username, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            self.driver.find_element(by, value).send_keys(username)
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _set_password_(self, password, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            self.driver.find_element(by, value).send_keys(password)
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _click_login_button_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.text_to_be_present_in_element((by, value), "Login"))
            self.driver.find_element(by, value).click()
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_(*MainPageLocators.ALERT)

    def login(self, username, password):
        """public method to login"""
        self._set_username_(username, *MainPageLocators.INPUT_USERNAME)
        self._set_password_(password, *MainPageLocators.INPUT_PASSWORD)
        self._click_login_button_(*MainPageLocators.BUTTON_LOGIN)


class AdminPage(BasePage):
    """Admin page class"""

    def _choose_position_in_navigation_menu_(self, position, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            elements = self.driver.find_elements(by, value)
            for element in elements:
                if element.text == position:
                    catalog = element
                    break
            catalog.click()
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _choose_catalog_element_(self, element_name, by, value, delay=5):
        """public method to choose position in catalog"""
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            catalog_elements = self.driver.find_elements(by, value)
            for catalog_element in catalog_elements:
                if catalog_element.text == element_name:
                    catalog_element.click()
                    break
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def choose_catalog(self):
        """public method to choose Catalog in menu"""
        self._choose_position_in_navigation_menu_("Catalog", *AdminPageLocators.CATALOG)

    def choose_product(self):
        """public method to choose Product"""
        self._choose_catalog_element_("Products", *AdminPageLocators.CATALOG_ELEMENTS)


class ProductPage(BasePage):
    """Product page class"""

    def _click_button_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((by, value)))
            element = self.driver.find_element(by, value).click()
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _click_product_navigation_tab_(self, tab_name, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            catalog_elements = self.driver.find_elements(by, value)
            for catalog_element in catalog_elements:
                if catalog_element.text == tab_name:
                    catalog_element.click()
                    break
            return catalog_element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _input_text_(self, text, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value).send_keys(text)
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _get_alert_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value).text
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _check_product_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value).click()
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _accept_delete_(self):
        self.driver.switch_to.alert.accept()

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_(*ProductPageLocators.ALERT_MODIFY_PRODUCT)

    def add_product(self, product_name, product_meta_tag_title, product_model):
        """public method to add product"""
        self._click_button_(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        self._click_product_navigation_tab_('General', *ProductPageLocators.TAB_NAVIGATION_PRODUCT)
        self._input_text_(product_name, *ProductPageLocators.INPUT_PRODUCT_NAME)
        self._input_text_(product_meta_tag_title, *ProductPageLocators.INPUT_PRODUCT_META_TAG_TITLE)
        self._click_product_navigation_tab_('Data', *ProductPageLocators.TAB_NAVIGATION_PRODUCT)
        self._input_text_(product_model, *ProductPageLocators.INPUT_PRODUCT_MODEL)
        self._click_button_(*ProductPageLocators.BUTTON_SAVE_PRODUCT)

    def delete_product(self):
        """public method to delete product"""
        self._check_product_(*ProductPageLocators.CHECKBOX_PRODUCT)
        self._click_button_(*ProductPageLocators.BUTTON_DELETE_PRODUCT)
        self._accept_delete_()

    def modify_product(self):
        """public method to modify product"""
        self._click_button_(*ProductPageLocators.BUTTON_MODIFY_PRODUCT)
        self._click_button_(*ProductPageLocators.BUTTON_SAVE_PRODUCT)
