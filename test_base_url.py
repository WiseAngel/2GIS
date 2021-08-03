import pytest
from deepdiff import DeepDiff
from requests import request


def count_regions_total():
    regions = []
    page = 1
    while True:
        response = request('GET', f'https://regions-test.2gis.com/1.0/regions?page={page}&page_size=15').json()
        if not response['items']:
            break
        regions += [*response['items']]
        page += 1 
    regions_without_duplicates = list({str(i):i for i in regions}.values())
    expected_total = len(regions_without_duplicates)
    return expected_total

@pytest.mark.xfail(reason='Total count hardcoded')
def test_total_counter_correspond_to_the_number_of_regions():
    response = request('GET', 'https://regions-test.2gis.com/1.0/regions').json()
    actual_total = response['total']
    expected_total = count_regions_total()
    assert actual_total == expected_total, f'Фактическое количество регионов: {expected_total} != Ожидаемому количесту регионов: {actual_total}'

 

def test_base_body():
    response = request('GET', 'https://regions-test.2gis.com/1.0/regions')
    body = response.json()
    tmp = {"total": 22, "items": [{"id": 196, "name": "\u0410\u043a\u0442\u0430\u0443", "code": "aktau", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 167, "name": "\u0410\u043a\u0442\u043e\u0431\u0435", "code": "aktobe", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 67, "name": "\u0410\u043b\u043c\u0430\u0442\u044b", "code": "almaty", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 112, "name": "\u0411\u0438\u0448\u043a\u0435\u043a", "code": "bishkek", "country": {"name": "\u041a\u044b\u0440\u0433\u044b\u0437\u0441\u0442\u0430\u043d", "code": "kg"}}, {"id": 114, "name": "\u0412\u043b\u0430\u0434\u0438\u043a\u0430\u0432\u043a\u0430\u0437", "code": "vladikavkaz", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 25, "name": "\u0412\u043b\u0430\u0434\u0438\u0432\u043e\u0441\u0442\u043e\u043a", "code": "vladivostok", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 105, "name": "\u0414\u043d\u0435\u043f\u0440", "code": "dnepropetrovsk", "country": {"name": "\u0423\u043a\u0440\u0430\u0438\u043d\u0430", "code": "ua"}}, {"id": 7, "name": "\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a", "code": "krasnoyarsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 26, "name": "\u041c\u0430\u0433\u043d\u0438\u0442\u043e\u0433\u043e\u0440\u0441\u043a", "code": "magnitogorsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 32, "name": "\u041c\u043e\u0441\u043a\u0432\u0430", "code": "moscow", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}]}
    ddiff = DeepDiff(body['items'][0], tmp['items'][0])
    ddiff_full = DeepDiff(body, tmp)
    assert ddiff == {}

@pytest.mark.xfail(reason='The number of items per page is changed by default to 10')
def test_base_page_size():
    response = request('GET', 'https://regions-test.2gis.com/1.0/regions')
    body = response.json()
    assert body['total'] == 22, f'Значение total: {body["total"]} != 22.'
    assert response.status_code == 200, f'status code 200 != {response.status_code}'
    assert len(body['items']) == 15, f'Length items != 15'