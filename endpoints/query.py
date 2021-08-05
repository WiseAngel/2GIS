import pytest

from endpoints import *

def check_message_about_query(response, value):
    if len(str(value)) <= 3:
        assert response["error"]["message"] == 'Параметр \'q\' должен быть не менее 3 символов', response["error"]["message"]
    else:
        assert response == {"total": 22, "items": []}, response
   
