import pytest
from requests import request
from deepdiff import DeepDiff

base_url = 'https://regions-test.2gis.com/1.0/regions'
endpoint = 'page_size'
positiv_value = [5, 10, 15]
negativ_value = [22, 0, -1, ' ', None]

def send_get_request(base_url, endpoint, value):
    url = f'{base_url}?{endpoint}={value}'
    response = request("GET", url)
    return response

def check_total(response):
    try:
        response['total'] == 22
    except KeyError:
        return False
    return True

def check_items_length(response, value):
    try:
        len(response['items']) == value
    except KeyError:
        return False
    return True

def test_base_body():
    response = request('GET', 'https://regions-test.2gis.com/1.0/regions')
    body = response.json()
    tmp = {"total": 22, "items": [{"id": 196, "name": "\u0410\u043a\u0442\u0430\u0443", "code": "aktau", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 167, "name": "\u0410\u043a\u0442\u043e\u0431\u0435", "code": "aktobe", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 67, "name": "\u0410\u043b\u043c\u0430\u0442\u044b", "code": "almaty", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 112, "name": "\u0411\u0438\u0448\u043a\u0435\u043a", "code": "bishkek", "country": {"name": "\u041a\u044b\u0440\u0433\u044b\u0437\u0441\u0442\u0430\u043d", "code": "kg"}}, {"id": 114, "name": "\u0412\u043b\u0430\u0434\u0438\u043a\u0430\u0432\u043a\u0430\u0437", "code": "vladikavkaz", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 25, "name": "\u0412\u043b\u0430\u0434\u0438\u0432\u043e\u0441\u0442\u043e\u043a", "code": "vladivostok", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 105, "name": "\u0414\u043d\u0435\u043f\u0440", "code": "dnepropetrovsk", "country": {"name": "\u0423\u043a\u0440\u0430\u0438\u043d\u0430", "code": "ua"}}, {"id": 7, "name": "\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a", "code": "krasnoyarsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 26, "name": "\u041c\u0430\u0433\u043d\u0438\u0442\u043e\u0433\u043e\u0440\u0441\u043a", "code": "magnitogorsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 32, "name": "\u041c\u043e\u0441\u043a\u0432\u0430", "code": "moscow", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}]}
    ddiff = DeepDiff(body['items'][0], tmp['items'][0])
    ddiff_full = DeepDiff(body, tmp)
    print (ddiff, ddiff_full)
    assert ddiff == {}


@pytest.mark.xfail(reason='The number of items per page is changed by default to 10')
def test_base_page_size(self):
    self.response = request('GET', 'https://regions-test.2gis.com/1.0/regions')
    self.body = self.response.json()
    assert self.body['total'] == 22, f'Значение total: {self.body["total"]} != 22.'
    assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'
    assert len(self.body['items']) == 15, f'Length items != 15'


@pytest.mark.parametrize('value', positiv_value)
class TestPositiv():

    def test_total_count(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        assert check_total(self.response), f'Значение {value}, не удовлетворяет условию. {self.response["error"]["message"]}'
        
    def test_items_count(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        assert check_items_length(self.response, value), f'Length items != {value} {self.response["error"]["message"]}'

    def test_items_count2(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        assert len(self.response['items']) == value, f'Length items != {value} {self.response["error"]["message"]}'

    def test_status_code_is_200(self, value):
        self.response = send_get_request(base_url, endpoint, value)
        assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'


@pytest.mark.parametrize('value', negativ_value)
class TestNegativ():
    # @pytest.mark.xfail(reason='Опечатка в слове "...должен..."')
    def test_message_about_invalid_parameters(self, value):
        self.response = send_get_request(base_url, endpoint, value).json() 
        if type(value) == int: 
            assert self.response["error"]["message"] == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15'
        else:
            assert self.response["error"]["message"] == 'Параметр \'page_size\' должен быть целым числом'

    def test_status_code_is_200(self, value):
        self.response = send_get_request(base_url, endpoint, value)
        assert self.response.status_code == 200, f'status code 200 != {self.response.status_code}'
   