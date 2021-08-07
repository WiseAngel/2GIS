import pytest

from endpoints import *


@pytest.mark.parametrize('value', page_size_positive_values)
class TestPositiv():
    
    sr = SendRequest()
        
    # The number of regions in the response is equal to the one passed in the request
    def test_items_count(self, value):
        response = self.sr.send_get_request(page_size_endpoint, value).json() 
        check_items_length(response, value)

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(page_size_endpoint, value)
        status_code_is_200(response, value)
    
    # Parameter total is equal to the total number of regions
    def test_total_count(self, value):
        response = self.sr.send_get_request(page_size_endpoint, value).json() 
        check_total(response)


@pytest.mark.parametrize('value', page_size_negative_values)
class TestNegativ():

    sr = SendRequest()

    # @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    # Correct message about invalid parameter values page_size
    def test_message_about_invalid_parameters(self, value):
        response = self.sr.send_get_request(page_size_endpoint, value).json() 
        check_message_about_invalid_parameters(response, value) 

    # Response status code 200    
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(page_size_endpoint, value) 
        status_code_is_200(response, value)
   