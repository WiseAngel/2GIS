def check_message_about_query(response, value):
    if len(str(value)) <= 3:
        assert response.get('error', {}).get('message', 'error.message не найден') == 'Параметр \'q\' должен быть не менее 3 символов', response.get('error', {}).get('message', 'error.message не найден')
    else:
        assert response == {"total": 22, "items": []}, response
   
