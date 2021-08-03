import pytest
from deepdiff import DeepDiff
from requests import request

from endpoints import *

positiv_value = [5, 10, 15]
negativ_value = [4, 6, 9, 11, 14, 16, 22, 1, 0, -1, '', None]

@pytest.mark.parametrize('value', positiv_value)
class TestPositiv():
    sr = SendRequest()

    def test_total_count(self, value):
        self.response = self.sr.send_get_request(Locators.ENDPOINT_PAGE_SIZE['name'], value).json() 
        check_total(self.response, 'total', 22)
        
    def test_items_count(self, value):
        self.response = self.sr.send_get_request(Locators.ENDPOINT_PAGE_SIZE['name'], value).json() 
        check_items_length(self.response, 'items', value)

    def test_status_code_is_200(self, value):
        self.response = self.sr.send_get_request(Locators.ENDPOINT_PAGE_SIZE['name'], value)
        status_code_is_200(self.response)


@pytest.mark.parametrize('value', negativ_value)
class TestNegativ():

    sr = SendRequest()
    # @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    def test_message_about_invalid_parameters(self, value):
        self.response = self.sr.send_get_request(Locators.ENDPOINT_PAGE_SIZE['name'], value).json() 
        check_message_about_invalid_parameters(self.response, value) 
        
    def test_status_code_is_200(self, value):
        self.response = self.sr.send_get_request(Locators.ENDPOINT_PAGE_SIZE['name'], value) 
        status_code_is_200(self.response)
   