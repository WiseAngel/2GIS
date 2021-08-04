import pytest

from endpoints import *



positive_values = Locators.ENDPOINTS['page_size']['values']['positive']
negative_values = Locators.ENDPOINTS['page_size']['values']['negative']

def foo(num):
    list_by_number_of_endpoints = []
    for i in range(num):
        list_by_number_of_endpoints.append([])
    print(list_by_number_of_endpoints)

    return list_by_number_of_endpoints

def bar(num, *value):
    list_by_number_of_endpoints = foo(num)
    for i, e in enumerate(value):
        print(f'i: {i}', f'e: {e}')
        for i, v in enumerate(e):
            if i < num:
                list_by_number_of_endpoints[i].append(v)
            else:
                break
    print(list_by_number_of_endpoints)

bar(3, [1,2,3], [4,5,6], [7,8,9,0])

@pytest.mark.parametrize('endpoint', [['page_size','page']])
@pytest.mark.parametrize( 'value', [[5, 1], [5, 2]])
def test_status_code_is_200(endpoint, value):
    sr = SendRequest()
    response = sr.send_get_request_with_multiple_parameters(endpoint, value)
    status_code_is_200(response)