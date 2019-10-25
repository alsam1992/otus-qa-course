"""Module with testsuite of tests for opencart tests"""
import time


class TestSuiteSSH:
    """Testsuite of tests for opencart services"""

    def test_apache_restart(self, apache_restart_test):
        """apache restart test"""
        expected_result, current_result = apache_restart_test
        assert expected_result == current_result

    def test_mysql_restart(self, mysql_restart_test):
        """mysql restart test"""
        expected_result, current_result = mysql_restart_test
        assert expected_result == current_result

    def test_reset(self, is_base_page, server_reset):
        """test for opencart server reset"""
        server_reset
        time.sleep(90)
        expected_result, current_result = is_base_page
        assert expected_result == current_result
