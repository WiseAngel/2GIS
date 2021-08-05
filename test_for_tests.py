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

# bar(3, [1,2,3], [4,5,6], [7,8,9,0])

# @pytest.mark.parametrize('endpoint', [['page_size','page']])
# @pytest.mark.parametrize( 'value', [[5, 1], [5, 2], [5, 3]])
# def test_status_code_is_200(endpoint, value):
#     sr = SendRequest()
#     response = sr.send_get_request_with_multiple_parameters(endpoint, value)
#     status_code_is_200(response)


# def count_country_code(*keys):
#     base_url = Locators.BASE_URL
#     regions = []
#     page = 1
#     while True:
#         response = request('GET', f'{base_url}?page={page}&page_size=15').json()
#         if not response['items']:
#             break
#         regions += [*response['items']]
#         page += 1 

    
#     regions_without_duplicates = list({i['country']['code']:i for i in regions})
#     regions_without_duplicates2 = list({i['id']:i for i in regions})
#     expected_total = len(regions_without_duplicates)
#     expected_total2 = len(regions_without_duplicates2)
#     print (expected_total, regions_without_duplicates)
#     print (expected_total2, regions_without_duplicates2)

# count_country_code(['country'],['code'])






# def count_regions_total():
#     base_url = Locators.BASE_URL
#     regions = []
#     page = 1
#     while True:
#         response = request('GET', f'{base_url}?page={page}&page_size=15').json()
#         if not response['items']:
#             break
#         regions += [*response['items']]
#         page += 1 
#     regions_without_duplicates = list({str(i):i for i in regions}.values())
#     expected_total = len(regions_without_duplicates)
#     return expected_total

# def count_country_code():
#     base_url = Locators.BASE_URL
#     regions = []
#     page = 1
#     while True:
#         response = request('GET', f'{base_url}?page={page}&page_size=15').json()
#         if not response['items']:
#             break
#         regions += [*response['items']]
#         page += 1 
#     regions_without_duplicates = list({i['country']['code']:i for i in regions}.values())
#     expected_total = len(regions_without_duplicates)
#     return expected_total
