import pytest
from deepdiff import DeepDiff
from requests import request

def check_total_counter_of_regions(actual, expected):
    actual_total = actual
    expected_total = expected
    assert actual_total == expected_total, \
        f'Фактическое количество регионов: {expected_total} != Ожидаемому количесту регионов: {actual_total}'

def check_body_padding(actual, expected):
    ddiff = DeepDiff(actual, expected)
    assert ddiff == {}, f'Ожидаемое и фактическое тело ответа не совпадают. Несоответствия: {ddiff}'
