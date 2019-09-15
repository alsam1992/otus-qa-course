"""Module contains Page-object classes"""
from locators import MainPageLocators
from locators import DownloadsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import os


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

    def _get_token_(self):
        text = self.get_url()
        start = (text.find('token=') + 6)
        return str(text[start:])

    def _get_alert_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.alert_is_present())
            element = self.driver.find_element(by, value)
            return element.text
        except NoAlertPresentException as err:
            raise err

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

    def get_token(self):
        """public method to get token"""
        return self._get_token_()


class LoginPage(BasePage):
    """Login page class"""

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


class DownloadsPage(BasePage):
    """Downloads page class"""

    def _get_file_alert_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element.text
        except NoAlertPresentException as err:
            raise err

    def navigate(self):
        """Public method to page navigate"""
        token = self.get_token()
        self.driver.get(DownloadsPageLocators.DOWNLOADS_PAGE_URL + token)
        self.driver.maximize_window()

    def get_file_alert(self):
        """public method to get add file alert"""
        return self._get_file_alert_(*DownloadsPageLocators.ADD_FILE_ALERT)

    def add_picture(self, description, mask):
        """Public method to add picture"""
        self.driver.find_element(*DownloadsPageLocators.BUTTON_ADD_NEW).click()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, DownloadsPageLocators.PICTURE_FILE_NAME)
        self.driver.find_element(*DownloadsPageLocators.INPUT_DOWNLOAD_DESCRIPTION).send_keys(description)
        self.driver.find_element(*DownloadsPageLocators.INPUT_MASK).send_keys(mask)
        JSCODE_1 = '''
            $(document).ready(function(){
                $('body').prepend('<form enctype="multipart/form-data" id="form-upload" style="display: none;"><input type="file" name="file" /></form>');
                $('#form-upload input[name=\\'file\\']');
            })
        '''
        JSCODE_4 = '''
                            if (typeof timer != 'undefined') {
                                clearInterval(timer);
                            }

                            timer = setInterval(function() {
                                if ($('#form-upload input[name=\\'file\\']').val() != '') {
                                    clearInterval(timer);

                                    $.ajax({
                                        url: 'http://127.0.0.1/opencart/admin/index.php?route=catalog/download/upload&user_token=''' + str(
            self._get_token_()) + '''',
                                        type: 'post',
                                        dataType: 'json',
                                        data: new FormData($('#form-upload')[0]),
                                        cache: false,
                                        contentType: false,
                                        processData: false,
        								beforeSend: function() {
        									$('#button-upload').button('loading');
        								},
        								complete: function() {
        									$('#button-upload').button('reset');
        								},
        								success: function(json) {
        									if (json['error']) {
        										alert(json['error']);
        									}

        									if (json['success']) {
        										alert(json['success']);

        										$('input[name=\\'filename\\']').val(json['filename']);
        										$('input[name=\\'mask\\']').val(json['mask']);
        									}
        								},
        								error: function(xhr, ajaxOptions, thrownError) {
        									alert(thrownError + xhr.statusText + xhr.responseText);
                                        }
                                    });
                                }
                            }, 500);
        '''

        self.driver.execute_script(JSCODE_1)
        self.driver.find_element(*DownloadsPageLocators.INPUT_MANAGER).send_keys(filename)
        self.driver.execute_script(JSCODE_4)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.driver.find_element(*DownloadsPageLocators.BUTTON_SAVE).click()
