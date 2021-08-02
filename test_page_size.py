import pytest
from requests import request

from pages import *

base_url = 'https://regions-test.2gis.com/1.0/regions'
endpoint = 'page_size'
positiv_value = [5, 10, 15]
negativ_value = [22, 0, -1, ' ', None]

def send_get_request(base_url, endpoint, value):
    url = f'{base_url}?{endpoint}={value}'
    response = request("GET", url)
    return response

@pytest.mark.xfail(reason='The number of items per page is changed by default to 10')
def test_base_page_size(self):
    self.response = request('GET', 'https://regions-test.2gis.com/1.0/regions')
    self.body = self.response.json()
    assert self.body['total'] == 22, f'Значение total: {self.body["total"]} != 22.'
    assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'
    assert len(self.body['items']) == 15, f'Length items != 15'


@pytest.mark.parametrize('value', positiv_value)
class TestPositiv():

    def test_total_count(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        assert check_total(self.response), f'Значение {value}, не удовлетворяет условию. {self.response["error"]["message"]}'
        
    def test_items_count(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        assert check_items_length(self.response, value), f'Length items != {value} {self.response["error"]["message"]}'

    def test_status_code_is_200(self, value):
        self.response = send_get_request(base_url, endpoint, value)
        assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'


@pytest.mark.parametrize('value', negativ_value)
class TestNegativ():
    # @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    def test_message_about_invalid_parameters(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        if type(value) == int: 
            assert self.response["error"]["message"] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15'
        else:
            assert self.response["error"]["message"] == 'Параметр \'page_size\' должен быть целым числом'

    def test_status_code_is_200(self, value):
        self.response = send_get_request(base_url, endpoint, value)
        assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'
   