def check_message_about_invalid_parameters(response, value):
    if type(value) == int: 
        assert response.get('error', {}).get('message', 'error.message не найден') == 'Параметр \'page_size\' может быть одним из следующих значений: 5, 10, 15', response.get('error', {}).get('message', 'error.message не найден')
    else:
        assert response.get('error', {}).get('message', 'error.message не найден') == 'Параметр \'page_size\' должен быть целым числом', response.get('error', {}).get('message', 'error.message не найден')

