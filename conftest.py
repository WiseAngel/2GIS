# import pytest
# from requests import request

# @pytest.fixture(scope='function')
# def send_get_request(base_url, endpoint, value):
#     url = f'{base_url}?{endpoint}={value}'
#     response = request("GET", url)
#     res = response.json()
#     return response