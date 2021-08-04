from requests import request
import pytest


def check_message_about_invalid_parameters(response, value):
    if type(value) == int: 
        assert response["error"]["message"] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15', response["error"]["message"]
    else:
        assert response["error"]["message"] == 'Параметр \'page_size\' должен быть целым числом', response["error"]["message"]

