import pytest
from deepdiff import DeepDiff
from requests import request

from .locators import Locators


class SendRequest():
   
    base_url = Locators.BASE_URL

    def send_get_request(self, endpoint, value):
        url = f'{self.base_url}?{endpoint}={value}'
        response = request("GET", url)
        return response

    def send_get_request_to_base_url(self):
        url = self.base_url
        response = request("GET", url)
        return response
    
    def send_get_request_with_multiple_parameters(self, endpoint: list, value: list):
        endpoints_arr = []
        for i, e in enumerate(endpoint):
            endpoints_arr.append(f'{e}={value[i]}')
        endpoints = '&'.join(endpoints_arr)
        url = f'{self.base_url}?{endpoints}'
        response = request("GET", url)
        return response

        
class CountRegions():
       
    def __init__(self):
        self.get_all_regions()
        self.get_regions_without_duplicates()

    base_url = Locators.BASE_URL
    regions: list
    regions_without_duplicates: list
    country_code_without_duplicates: list
    len_regions: int
    len_country_codes: int
    
    def get_all_regions(self):
        page = 1
        regions = []
        while True:
            response = request('GET', f'{self.base_url}?page={page}&page_size=15').json()
            if not response['items']:
                break
            regions += [*response['items']]
            page += 1 
        self.regions = regions
        return self.regions

    def get_regions_without_duplicates(self):
        self.regions_without_duplicates = list({str(i):i for i in self.regions}.values())
        return self.regions_without_duplicates

    def get_country_codes(self):
        self.country_code_without_duplicates = list({i['country']['code']:i for i in self.regions})
        return self.country_code_without_duplicates 

    def count_regions_total(self):
        self.len_regions = len(self.regions_without_duplicates)
        return self.len_regions

    def count_country_code(self):
        self.len_country_codes = len(self.country_code_without_duplicates)
        return self.len_country_codes


#############################################################################################################


def check_body_padding(actual, expected):
    ddiff = DeepDiff(actual, expected)
    assert ddiff == {}, \
        f'Ожидаемое и фактическое тело ответа не совпадают. Несоответствия: {ddiff}'

def status_code_is_200(response, value='Нет данных'):
    assert response.status_code == 200, f'{value} # status code в ответе: {response.status_code}. Ожидал: 200.'

def check_items_length(response, value=15):
    response_len = len(response['items'])
    assert response_len == value, \
        f'Кол-во регионов в ответе {response_len}, ожидали получить {value}'

def check_total(response):
    total = Locators.TOTAL_REGIONS
    total_key = list(total.keys())[0]
    assert response[total_key] == total[total_key], \
        f'Значение {total_key} равно {response[total_key]}, ожидали {total[total_key]}'

def check_total_counter_of_regions(actual, expected):
    actual_total = actual
    expected_total = expected
    assert actual_total == expected_total, \
        f'Фактическое количество регионов: {expected_total} != Ожидаемому количесту регионов: {actual_total}'
