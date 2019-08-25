""" API tests for https://dog.ceo/dog-api/ """

import pytest

ENDPOINTS = [
    '/breeds/list/all',
    '/breeds/image/random',
    '/breeds/image/random/10',
    '/breed/akita/images',
    '/breed/akita/images/random/10',
    '/breed/spaniel/list',
    '/breed/spaniel/images',
    '/breed/spaniel/cocker/images/random',
    '/breed/spaniel/cocker/images/random/10',
]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_dogapi(dogceo, endpoint):
    """ Test GET requests for https://dog.ceo/api """
    response = dogceo.do_get(endpoint)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert response.headers['Content-Type'] == 'application/json'
