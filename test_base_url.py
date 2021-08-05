import pytest

from endpoints import *

class TestBaseURL():
    
    sr = SendRequest()

    # The number of regions in the response is equal to the one passed in the request
    @pytest.mark.xfail(reason='The number of items per page is changed by default to 10')
    def test_items_count(self):
        body = self.sr.send_get_request_to_base_url().json()
        check_items_length(body)

    def test_response_from_base_URL_is_equal_to_response_from_first_page(self):
        body = self.sr.send_get_request_to_base_url().json()
        reference_body = self.sr.send_get_request('page', 1).json()
        check_body_padding(body, reference_body)

    # Response status code 200
    def test_status_code_is_200(self):
        response = self.sr.send_get_request_to_base_url()
        status_code_is_200(response)

    # Parameter total is equal to the total number of regions
    def test_total_count(self):
        body = self.sr.send_get_request_to_base_url().json()
        check_total(body)
