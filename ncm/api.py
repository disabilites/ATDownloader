from ncm.constants import api_url

import requests
import json

class CloudmusicAPI(object):

    def __init__(self):
        super().__init__()
        self.se = requests.session()
        self.timeout = 10
        self.headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Accept': '*/*'
        }

    def get_song(self, content):
        params = {'type': 'search', 'search_type': '1', 's': content, 'limit': '10'}
        result = requests.get(api_url, params=params).text
        data = json.loads(result)
        return data

    def get_playlist(self, content):
        params = {'type': 'search', 'search_type': '1000', 's': content}
        result = requests.get(api_url, params=params)
        result_json = json.loads(result)
        return result_json