from requests import request
import pytest
from .locators import Locators


class SendRequest():
   
    base_url = Locators.BASE_URL


    def send_get_request(self, endpoint, value):
        self.url = f'{self.base_url}?{endpoint}={value}'
        response = request("GET", self.url)
        return response

    # def send_get_request1(self):
    #     url = f'{self.base_url}?{self.endpoint}={self.value}'
    #     response = request("GET", url)
    #     return response