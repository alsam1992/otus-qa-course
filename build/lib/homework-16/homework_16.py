"""Module with testsuite of tests for JSON API tests"""


class TestSuite:
    """Testsuite for base page tests"""

    def test_add_product(self, add_product):
        """add product test positive scenario"""
        expected_result, current_result = add_product
        assert expected_result in current_result

    # def test_modify_product(self, modify_product):
    #    """modify product test positive scenario"""
    #    expected_result, current_result = modify_product
    #    assert expected_result in current_result

    # def test_delete_product(self, delete_product):
    #    """delete product test positive scenario"""
    #    expected_result, current_result = delete_product
    #    assert expected_result in current_result
