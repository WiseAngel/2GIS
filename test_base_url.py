import pytest

from endpoints import *


# The number of regions in the response is equal to the one passed in the request
@pytest.mark.xfail(reason='The number of items per page is changed by default to 10')
def test_items_count():
    sr = SendRequest()
    body = sr.send_get_request_to_base_url().json()
    check_items_length(body)

# Response status code 200
def test_status_code_is_200():
    sr = SendRequest()
    response = sr.send_get_request_to_base_url()
    status_code_is_200(response)

# Parameter total is equal to the total number of regions
def test_total_count():
    sr = SendRequest()
    body = sr.send_get_request_to_base_url().json()
    check_total(body)
