import pytest

from endpoints import *


positive_values = Locators.ENDPOINTS['page']['values']['positive']
negative_values = Locators.ENDPOINTS['page']['values']['negative']
ENDPOINT = Locators.ENDPOINTS['page']['name']

@pytest.mark.parametrize('value', positive_values)
class TestPositiv():
    
    sr = SendRequest()
    cr = CountRegions()

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(ENDPOINT, value)
        status_code_is_200(response)
    
    # Parameter total is equal to the total number of regions
    def test_total_count(self, value):
        response = self.sr.send_get_request(ENDPOINT, value).json() 
        check_total(response)

@pytest.mark.parametrize('value', negative_values)
class TestNegativ():

    sr = SendRequest()

    # Correct message about invalid parameter values page_size
    @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    def test_message_about_invalid_parameters(self, value):
        response = self.sr.send_get_request(ENDPOINT, value).json() 
        check_message_about_invalid_page(response)    

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(ENDPOINT, value)
        status_code_is_200(response)
