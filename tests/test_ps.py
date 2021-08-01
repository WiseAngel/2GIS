from requests import request
import pytest
endpoint = 'https://regions-test.2gis.com/1.0/regions'
values = [5, 10, 15]

@pytest.mark.parametrize('value', values)
def test_ps():
    print(endpoint)
    url = f'{endpoint}?page_size='
    ps = [5, 10, 15]
    payload = {}
    headers = {}
    for i in ps:

        response = request(
            "GET", url+str(i), headers=headers, data=payload)
        res = response.json()

        assert res['total'] == 22, 'total'
        assert response.status_code == 200, 'status code'
        assert len(res['items']) == i, 'len'