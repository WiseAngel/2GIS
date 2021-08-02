from requests import request
import pytest

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