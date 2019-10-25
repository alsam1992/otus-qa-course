"""Module with testsuite of tests for http socket tests"""


class TestSuiteSocket:
    """Testsuite of tests for http socket"""

    def test_http_socket(self, http):
        """http thought socket test"""
        header, retcode, retresult, headers = http
        assert retresult == "OK"
