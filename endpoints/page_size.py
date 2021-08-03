from requests import request
import pytest


def check_total(response, key, value):
    response[key] == value
    assert response[key] == value, f'Значение {key} равно {response[key]}, ожидали {value}'

def check_items_length(response, key, value):
    response_len = len(response[key])
    assert response_len == value, f'Кол-во регионов в ответе {response_len}, ожидали получить {value}'

def status_code_is_200(response):
    assert response.status_code == 200, f'status code в ответе: {response.status_code}. Ожидал: 200'

def check_message_about_invalid_parameters(response, value):
    if type(value) == int: 
        assert response["error"]["message"] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15', response["error"]["message"]
    else:
        assert response["error"]["message"] == 'Параметр \'page_size\' должен быть целым числом', response["error"]["message"]

