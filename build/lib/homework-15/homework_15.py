"""Module with testsuite parscing log and save to json file"""


class TestSuite:
    """Testsuite for log parcing tests"""

    def test_log_parcer(self, log_parcer):
        """log parcing test"""
        expected_result, current_result = log_parcer
        assert expected_result == current_result
