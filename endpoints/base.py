from requests import request
import pytest
from .locators import Locators


class SendRequest():
   
    base_url = Locators.BASE_URL


    def send_get_request(self, endpoint, value):
        self.url = f'{self.base_url}?{endpoint}={value}'
        response = request("GET", self.url)
        return response

    def send_get_request_to_base_url(self):
        url = self.base_url
        response = request("GET", url)
        return response