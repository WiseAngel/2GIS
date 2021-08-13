import pytest

from endpoints import *


sr = SendRequest()
dg = DataGenerator(page_size_positive_values, page_positive_values, q_positive_values)
v1 = dg.bar()
print()
print()
dg2 = DataGenerator(page_size_negative_values, page_negative_values)
v = dg2.bar()


# @pytest.mark.parametrize('endpoint', [['page_size','page']])
# @pytest.mark.parametrize('value', [*v])
# def test_status_code_is_200(endpoint, value):
#     response = sr.send_get_request_with_multiple_parameters(endpoint, value)
#     status_code_is_200(response, value)

# # Parameter total is equal to the total number of regions
# @pytest.mark.parametrize('endpoint', [['page_size','page', 'q']])
# @pytest.mark.parametrize('value', [*v1])
# def test_total_count(endpoint, value):
#     response = sr.send_get_request_with_multiple_parameters(endpoint, value).json() 
#     check_total(response)
import time
time.sleep(5)
print()
print()
dg3 = DataGenerator(page_size_positive_values, country_code_positive_values)
v2 = dg3.bar()