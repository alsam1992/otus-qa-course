"""Module with fixtures for tests"""

import pytest


@pytest.fixture(scope='module', autouse=True)
def module_data():
    """Fixture for module"""
    print("Module setup")
    print(module_data.__doc__)
    yield
    print("Module teardown")


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    """Fixture for testsuite"""
    print("Suite setup")
    print(suite_data.__doc__)
    yield
    print("Suite teardown")


@pytest.fixture(scope='function', autouse=True)
def case_data():
    """Fixture for testcase"""
    print("Case setup")
    print(case_data.__doc__)
    yield
    print("Case teardown")
