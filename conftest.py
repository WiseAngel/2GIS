# import pytest
# from requests import request
# base_url = 'https://regions-test.2gis.com/1.0/regions'
# endpoint = 'page_size'

# @pytest.fixture
# def send_get_request1(base_url, endpoint, value):
#     base_url:str
#     endpoint:str
#     value:int

#     url = f'{base_url}?{endpoint}={value}'
#     response = request("GET", url)
#     res = response.json()
#     return response


# L=[{"id": 196, "name": "\u0410\u043a\u0442\u0430\u0443", "code": "aktau", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, 
# {"id": 167, "name": "\u0410\u043a\u0442\u043e\u0431\u0435", "code": "aktobe", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, 
# {"id": 67, "name": "\u0410\u043b\u043c\u0430\u0442\u044b", "code": "almaty", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}},
# {"id": 196, "name": "\u0410\u043a\u0442\u0430\u0443", "code": "aktau", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, 
# {"id": 167, "name": "\u0410\u043a\u0442\u043e\u0431\u0435", "code": "aktobe", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}, 
# {"id": 67, "name": "\u0410\u043b\u043c\u0430\u0442\u044b", "code": "almaty", "country": {"name": "\u041a\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043d", "code": "kz"}}]
# k = list({str(i):i for i in L}.values())
# print (k)