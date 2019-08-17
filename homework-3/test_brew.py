import pytest
import requests


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)


import pytest

ENDPOINTS = [
    '/breweries',
    '/breweries?by_state=maine',
    '/breweries?by_state=california&by_type=brewpub',
    '/breweries?per_page=10&page=17',
    '/breweries/autocomplete?query=wolf',
    '/breweries?by_name=brew',
    '/breweries?by_city=chicago&sort='
    '/breweries?by_city=miami&sort=+type&per_page=10&page=1',
]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_brewery(openbrewery, endpoint):
    """ Test GET requests for https://api.openbrewerydb.org """
    response = openbrewery.do_get(endpoint)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
