
api_url = 'https://api.imjad.cn/hitokoto/'

def get_params(cat):
    params = {'cat': cat, 'charset': 'utf-8', 'encode': 'json'}
    return params