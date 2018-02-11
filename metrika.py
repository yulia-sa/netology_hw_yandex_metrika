import requests
import pprint
from urllib.parse import urlencode


APP_ID = '42171bff818849478f9b07bc7169b089'
AUTH_URL = 'https://oauth.yandex.ru/authorize'


auth_url_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTH_URL, urlencode(auth_url_data))))

# FILL ME
TOKEN = ''
COUNTER_ID = ''


class YandexMetrikaHeaders:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }


class YandexMetrikaUser(YandexMetrikaHeaders):
    def __init__(self, token):
        YandexMetrikaHeaders.__init__(self, token)
        self.token = token

    def get_counter_list(self):
        headers = YandexMetrikaHeaders.get_headers(self)
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',
                                headers=headers, params={'pretty': 1})
        return response.json()


class YandexMetrikaStatistics(YandexMetrikaHeaders):
    def __init__(self, token):
        YandexMetrikaHeaders.__init__(self, token)
        self.token = token

    def get_counter_visits(self, counter_id):
        headers = YandexMetrikaHeaders.get_headers(self)
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', 
                                params, headers=headers)
        return response.json()

    def get_counter_pageviews(self, counter_id):
        headers = YandexMetrikaHeaders.get_headers(self)
        params = {
            'id': counter_id,
            'metrics': 'ym:pv:pageviews'
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', 
                                params, headers=headers)
        return response.json()

    def get_counter_users(self, counter_id):
        headers = YandexMetrikaHeaders.get_headers(self)
        params = {
            'id': counter_id,
            'metrics': 'ym:pv:users'
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', 
                                params, headers=headers)
        return response.json()

# yulia = YandexMetrikaUser(TOKEN)

# counters = yulia.get_counter_list()
# pprint.pprint(counters)
# print('=================================')

statistics = YandexMetrikaStatistics(TOKEN)

visits = statistics.get_counter_visits(COUNTER_ID)
pprint.pprint(visits)
print('=================================')

pageviews = statistics.get_counter_pageviews(COUNTER_ID)
pprint.pprint(pageviews)
print('=================================')

users = statistics.get_counter_users(COUNTER_ID)
pprint.pprint(users)
print('=================================')
