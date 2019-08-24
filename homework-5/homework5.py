"""Module with testsuite of tests for JSON API tests"""
from LoginPage import LoginPage


class TestSuite:
    """Testsuite for base page tests"""

    def test_is_base_page(self, get_driver, cmdopt_url):
        """test for is base page"""
        login_page = LoginPage(get_driver, cmdopt_url)
        login_page.navigate()
        assert "Your Store" in login_page.get_title()
