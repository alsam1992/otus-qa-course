"""Module with testsuite of tests for JSON API tests"""
import pytest
import allure


class TestSuite:
    """Testsuite for base page tests"""

    @allure.title("This title will be replaced in a test body")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_positive(self, login_positive, cmdopt_browser, cmdopt_url):
        """login test positive scenario"""
        expected_result, current_result = login_positive
        assert expected_result in current_result
        allure.dynamic.title(
            'Успешное прохождение теста с логированием. browser_type: {}, url: {}'.format(cmdopt_browser, cmdopt_url))

    @pytest.mark.xfail(reason="wrong password test")
    @allure.title("Тест негативного сценария логирования")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_negative(self, login_negative, cmdopt_browser, cmdopt_url):
        """login test negative scenario"""
        expected_result, current_result = login_negative
        assert expected_result in current_result

    @pytest.mark.xfail(reason="wrong password test")
    @allure.title("Тест оправки пустой формы")
    @allure.severity(allure.severity_level.MINOR)
    def test_empty_form(self, empty_form, cmdopt_browser, cmdopt_url):
        """empty login form scenario"""
        expected_result, current_result = empty_form
        assert expected_result in current_result
