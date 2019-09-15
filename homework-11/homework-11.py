"""Module with testsuite of tests"""


class TestSuite:
    """Testsuite for upload picture tests on download menu page"""

    def test_login(self, login, add_picture):
        """add file test"""
        expected_result, current_result = add_picture
        assert expected_result in current_result
