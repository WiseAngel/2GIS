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
                              'negative': [1.1, -1, '', None]}}}
    TOTAL_REGIONS = {'total': 22}
