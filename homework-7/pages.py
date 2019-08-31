"""Module contains Page-object classes"""
from locators import ProductPageLocators


class BasePage(object):
    """Base page class"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def _get_title_(self):
        return self.driver.title

    def _click_close_modal_window_button_(self):
        self.driver.find_element(*MainPageLocators.CLOSE_MODAL_WINDOW).click()

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

    def _get_alert_(self):
        return self.driver.find_element(*MainPageLocators.ALERT).text

    def _set_username_(self, username):
        self.driver.find_element(*MainPageLocators.INPUT_USERNAME).send_keys(username)

    def _set_password_(self, password):
        self.driver.find_element(*MainPageLocators.INPUT_PASSWORD).send_keys(password)

    def _click_login_button_(self):
        self.driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_()

    def login(self, username, password):
        """public method to login"""
        self._set_username_(username)
        self._set_password_(password)
        self._click_login_button_()


class AdminPage(BasePage):
    """Admin page class"""

    def choose_catalog(self):
        """public method to choose catalog in menu"""
        elements = self.driver.find_elements(*AdminPageLocators.CATALOG)
        for element in elements:
            if element.text == "Catalog":
                catalog = element
                break
        catalog.click()

    def choose_catalog_element(self, element_name):
        """public method to choose catalog element"""
        catalog_elements = self.driver.find_elements(*AdminPageLocators.CATALOG_ELEMENTS)
        for catalog_element in catalog_elements:
            if catalog_element.text == element_name:
                catalog_element.click()
                break


class ProductPage(BasePage):
    """Product page class"""

    def _click_add_product_button_(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT).click()

    def _click_copy_product_button_(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT).click()

    def _click_delete_product_button_(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_DELETE_PRODUCT).click()

    def _click_product_navigation_tab_(self, tab_name):
        catalog_elements = self.driver.find_elements(*ProductPageLocators.TAB_NAVIGATION_PRODUCT)
        for catalog_element in catalog_elements:
            if catalog_element.text == tab_name:
                catalog_element.click()
                break

    def _set_product_name_(self, product_name):
        self.driver.find_element(*ProductPageLocators.INPUT_PRODUCT_NAME).send_keys(product_name)

    def _set_product_meta_tag_title_(self, product_meta_tag_title):
        self.driver.find_element(*ProductPageLocators.INPUT_PRODUCT_META_TAG_TITLE).send_keys(product_meta_tag_title)

    def _set_product_model_(self, product_model):
        self.driver.find_element(*ProductPageLocators.INPUT_PRODUCT_MODEL).send_keys(product_model)

    def _click_save_product_button_(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_SAVE_PRODUCT).click()

    def _get_alert_(self):
        return self.driver.find_element(*ProductPageLocators.ALERT_MODIFY_PRODUCT).text

    def _check_product_(self):
        self.driver.find_element(*ProductPageLocators.CHECKBOX_PRODUCT).click()

    def _accept_delete_(self):
        self.driver.switch_to.alert.accept()

    def _click_modify_product_button_(self):
        self.driver.find_element(*ProductPageLocators.BUTTON_MODIFY_PRODUCT).click()

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_()

    def add_product(self, product_name, product_meta_tag_title, product_model):
        """public method to add product"""
        self._click_add_product_button_()
        self._click_product_navigation_tab_('General')
        self._set_product_name_(product_name)
        self._set_product_meta_tag_title_(product_meta_tag_title)
        self._click_product_navigation_tab_('Data')
        self._set_product_model_(product_model)
        self._click_save_product_button_()

    def delete_product(self):
        """public method to delete product"""
        self._check_product_()
        self._click_delete_product_button_()
        self._accept_delete_()

    def modify_product(self):
        """public method to modify product"""
        self._click_modify_product_button_()
        self._click_save_product_button_()
