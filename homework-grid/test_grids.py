"""Module with testsuite of tests for JSON API tests"""


class TestSuite:
    """Testsuite for base page tests"""
    def test_login_positive(self, login_positive):
        """login test positive scenario"""
        expected_result, current_result = login_positive
        assert expected_result in current_result

    def test_login_negative(self, login_negative):
        """login test negative scenario"""
        expected_result, current_result = login_negative
        assert expected_result in current_result

    def test_empty_form(self, empty_form):
        """empty login form scenario"""
        expected_result, current_result = empty_form
        assert expected_result in current_result
