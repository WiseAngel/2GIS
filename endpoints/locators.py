class Locators():
    BASE_URL = 'https://regions-test.2gis.com/1.0/regions'
    ENDPOINTS = {'page_size': {'name': 'page_size',
                               'values': {
                                   'positive': [5, 10, 15],
                                   'negative': [4, 6, 9, 11, 14, 16, 22, 1, 0, -1, '', None]}},
                 'country_code': {'name': 'country_code',
                                  'values': {
                                      'positive': ['ru', 'kg', 'kz', 'cz'],
                                      'negative': ['ru1', 'ua', 'RU', 'None', '', ' ', None, 1, -1, 0]}},
                 'q': {'name': 'q',
                       'values': {
                           'positive': ['Омск', 'Новоссибирск', 'Нов', 'рск', 'ОМСК', 'астана'],
                           'negative': ['Ом', '/омск', 'zk', 'None', '', ' ', None, 1, -1, 0]}},
                 'page': {'name': 'page',
                          'values': {
                              'positive': [1, 2, 3, 100],
                              'negative': [1.1, -1, '', ' ', None, 0]}}}
    TOTAL_REGIONS = {'total': 22}

q_positive_values = Locators.ENDPOINTS['q']['values']['positive']
q_negative_values = Locators.ENDPOINTS['q']['values']['negative']
q_endpoint = Locators.ENDPOINTS['q']['name']

page_positive_values = Locators.ENDPOINTS['page']['values']['positive']
page_negative_values = Locators.ENDPOINTS['page']['values']['negative']
page_endpoint = Locators.ENDPOINTS['page']['name']

page_size_positive_values = Locators.ENDPOINTS['page_size']['values']['positive']
page_size_negative_values = Locators.ENDPOINTS['page_size']['values']['negative']
page_size_endpoint = Locators.ENDPOINTS['page_size']['name']

country_code_positive_values = Locators.ENDPOINTS['country_code']['values']['positive']
country_code_negative_values = Locators.ENDPOINTS['country_code']['values']['negative']
country_code_endpoint = Locators.ENDPOINTS['country_code']['name']