def check_message_about_invalid_region_code(response):
    assert response.get('error', {}).get('message', 'error.message не найден') == 'Параметр \'country_code\' может быть одним из следующих значений: ru, kg, kz, cz', \
        response.get('error', {}).get('message', 'error.message не найден')

def match_with_specification(actual, expected):
    result = [item for item in actual if item not in expected]
    assert result == [], f'Присутствуют сторонние регионы: {result}' 
