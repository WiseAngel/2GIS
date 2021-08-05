import pytest

from endpoints import *

def check_message_about_invalid_page(response):
    assert response["error"]["message"] == 'Параметр \'page\' должен быть целым числом', response["error"]["message"]
   

   
   