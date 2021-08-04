import pytest

from endpoints import *

positive_values = Locators.ENDPOINTS['page_size']['values']['positive']
negative_values = Locators.ENDPOINTS['page_size']['values']['negative']

@pytest.mark.parametrize('value', positive_values)
class TestPositiv():
    
    ENDPOINT_PAGE_SIZE = Locators.ENDPOINTS['page_size']['name']
    sr = SendRequest()
        
    # The number of regions in the response is equal to the one passed in the request
    def test_items_count(self, value):
        response = self.sr.send_get_request(self.ENDPOINT_PAGE_SIZE, value).json() 
        check_items_length(response, value)

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(self.ENDPOINT_PAGE_SIZE, value)
        status_code_is_200(response)
    
    # Parameter total is equal to the total number of regions
    def test_total_count(self, value):
        response = self.sr.send_get_request(self.ENDPOINT_PAGE_SIZE, value).json() 
        # check_total(self.response, 'total', 22)
        check_total(response)


@pytest.mark.parametrize('value', negative_values)
class TestNegativ():

    ENDPOINT_PAGE_SIZE = Locators.ENDPOINTS['page_size']['name']
    sr = SendRequest()

    # @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    # Correct message about invalid parameter values page_size
    def test_message_about_invalid_parameters(self, value):
        response = self.sr.send_get_request(self.ENDPOINT_PAGE_SIZE, value).json() 
        check_message_about_invalid_parameters(response, value) 

    # Response status code 200    
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(self.ENDPOINT_PAGE_SIZE, value) 
        status_code_is_200(response)
   