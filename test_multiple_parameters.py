import pytest

from endpoints import *

dg = DataGenerator()
v = dg.bar(page_size_positive_values, page_negative_values)
v1 = dg.bar(page_size_positive_values, page_negative_values, q_positive_values )

@pytest.mark.parametrize('endpoint', [['page_size','page', 'q']])
@pytest.mark.parametrize( 'value', [*v1])
def test_status_code_is_200(endpoint, value):
    sr = SendRequest()
    response = sr.send_get_request_with_multiple_parameters(endpoint, value)
    status_code_is_200(response)
