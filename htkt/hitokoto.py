from htkt.constants import *

import requests
import json

def get_hitokoto(cat=None):
    hitokoto = requests.get(api_url, get_params(cat=cat)).text
    hitokoto_json = json.loads(hitokoto)
    print(hitokoto_json['hitokoto'] + '     —— ' + hitokoto_json['source'])