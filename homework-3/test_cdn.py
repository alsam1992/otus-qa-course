""" API tests for https://cdnjs.com/api/ """

import pytest

ENDPOINTS = [
    '/libraries',
    '/libraries?search=react',
    '/libraries?search=react&fields=version',
    '/libraries?search=react&fields=assets',
    '/libraries/async',
]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_cdnjs(cdnjs, endpoint):
    """ Test GET requests for https://api.cdnjs.com """
    response = cdnjs.do_get(endpoint)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
