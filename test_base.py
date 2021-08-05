import pytest

from endpoints import *

class TestBaseResponse():
    
    sr = SendRequest()
    cr = CountRegions()

    def test_filing_response_body(self):
        body = self.sr.send_get_request_to_base_url().json()
        reference_body = {"total": 22, "items": [{"id": 196, "name": "\u0410\u043a\u0442\u0430\u0443", "code": "aktau", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 167, "name": "\u0410\u043a\u0442\u043e\u0431\u0435", "code": "aktobe", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 67, "name": "\u0410\u043b\u043c\u0430\u0442\u044b", "code": "almaty", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, {"id": 112, "name": "\u0411\u0438\u0448\u043a\u0435\u043a", "code": "bishkek", "country": {"name": "\u041a\u044b\u0440\u0433\u044b\u0437\u0441\u0442\u0430\u043d", "code": "kg"}}, {"id": 114, "name": "\u0412\u043b\u0430\u0434\u0438\u043a\u0430\u0432\u043a\u0430\u0437", "code": "vladikavkaz", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 25, "name": "\u0412\u043b\u0430\u0434\u0438\u0432\u043e\u0441\u0442\u043e\u043a", "code": "vladivostok", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 105, "name": "\u0414\u043d\u0435\u043f\u0440", "code": "dnepropetrovsk", "country": {"name": "\u0423\u043a\u0440\u0430\u0438\u043d\u0430", "code": "ua"}}, {"id": 7, "name": "\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a", "code": "krasnoyarsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 26, "name": "\u041c\u0430\u0433\u043d\u0438\u0442\u043e\u0433\u043e\u0440\u0441\u043a", "code": "magnitogorsk", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}, {"id": 32, "name": "\u041c\u043e\u0441\u043a\u0432\u0430", "code": "moscow", "country": {"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "code": "ru"}}]}
        # ddiff = DeepDiff(body['items'][0], reference_body['items'][0])
        check_body_padding(body, reference_body)

    @pytest.mark.xfail(reason='Total count hardcoded')
    def test_total_counter_correspond_to_the_number_of_regions(self):
        body = self.sr.send_get_request_to_base_url().json()
        actual_total = body['total']
        expected_total = self.cr.count_regions_total()
        check_total_counter_of_regions(actual_total, expected_total)