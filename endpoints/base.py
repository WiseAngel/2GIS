import pytest
from deepdiff import DeepDiff
from requests import request

from .locators import Locators


class SendRequest():
   
    base_url = Locators.BASE_URL

    def send_get_request(self, endpoint, value):
        self.url = f'{self.base_url}?{endpoint}={value}'
        response = request("GET", self.url)
        return response

    def send_get_request_to_base_url(self):
        url = self.base_url
        response = request("GET", url)
        return response

def count_regions_total():
    base_url = Locators.BASE_URL
    regions = []
    page = 1
    while True:
        response = request('GET', f'{base_url}?page={page}&page_size=15').json()
        if not response['items']:
            break
        regions += [*response['items']]
        page += 1 
    regions_without_duplicates = list({str(i):i for i in regions}.values())
    expected_total = len(regions_without_duplicates)
    return expected_total


#############################################################################################################


def check_body_padding(actual, expected):
    ddiff = DeepDiff(actual, expected)
    assert ddiff == {}, f'Ожидаемое и фактическое тело ответа не совпадают. Несоответствия: {ddiff}'

def status_code_is_200(response):
    assert response.status_code == 200, f'status code в ответе: {response.status_code}. Ожидал: 200'

def check_items_length(response, value=15):
    response_len = len(response['items'])
    assert response_len == value, f'Кол-во регионов в ответе {response_len}, ожидали получить {value}'

def check_total(response):
    total = Locators.TOTAL_REGIONS
    total_key = list(Locators.TOTAL_REGIONS.keys())[0]
    assert response[total_key] == total[total_key], \
        f'Значение {total_key} равно {response[total_key]}, ожидали {total[total_key]}'

def check_total_counter_of_regions(actual, expected):
    actual_total = actual
    expected_total = expected
    assert actual_total == expected_total, \
        f'Фактическое количество регионов: {expected_total} != Ожидаемому количесту регионов: {actual_total}'


