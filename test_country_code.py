import pytest

from endpoints import *


positive_values = Locators.ENDPOINTS['country_code']['values']['positive']
negative_values = Locators.ENDPOINTS['country_code']['values']['negative']

def test_match_codes_with_spec():
    cr = CountRegions()
    actual_codes = cr.get_country_codes()
    match_with_specification(actual_codes, positive_values)

@pytest.mark.parametrize('value', positive_values)
class TestPositiv():
    
    ENDPOINT = Locators.ENDPOINTS['country_code']['name']

    sr = SendRequest()
    cr = CountRegions()

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(self.ENDPOINT, value)
        status_code_is_200(response)
    
    # Parameter total is equal to the total number of regions
    def test_total_count(self, value):
        response = self.sr.send_get_request(self.ENDPOINT, value).json() 
        check_total(response)


    def test_response_contains_only_transmitted_region_codes(self, value):
        response = self.sr.send_get_request_with_multiple_parameters([self.ENDPOINT, 'page_size'], [value, 15]).json()
        country_code_without_duplicates = list({i['country']['code']:i for i in response['items']})
        match_with_specification(country_code_without_duplicates, value)

@pytest.mark.parametrize('value', negative_values)
class TestNegativ():

    ENDPOINT = Locators.ENDPOINTS['country_code']['name']
    sr = SendRequest()

    # Correct message about invalid parameter values page_size
    def test_message_about_invalid_parameters(self, value):
        response = self.sr.send_get_request(self.ENDPOINT, value).json() 
        check_message_about_invalid_region_code(response)    

    # Response status code 200
    def test_status_code_is_200(self, value):
        response = self.sr.send_get_request(self.ENDPOINT, value)
        status_code_is_200(response)
