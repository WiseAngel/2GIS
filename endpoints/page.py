def check_message_about_invalid_page(response):
    assert response.get('error', {}).get('message', 'error.message не найден') == 'Параметр \'page\' должен быть целым числом', response.get('error', {}).get('message', 'error.message не найден')
   

   
   