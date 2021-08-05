import pytest

from endpoints import *


def check_message_about_invalid_region_code(response):
    assert response["error"]["message"] == 'Параметр \'country_code\' может быть одним из следующих значений: ru, kg, kz, cz', \
        response["error"]["message"]

def match_with_specification(actual, expected):
    result = [item for item in actual if item not in expected]
    assert result == [], f'Присутствуют сторонние регионы: {result}' 

# def response_contains_only_transmitted_region_codes(actual, expected):

   