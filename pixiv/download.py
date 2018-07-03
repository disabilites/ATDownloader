from pixiv.constants import *
from pixiv.config import *

import requests
import json

def download_img_original(illust_id, down_path):
    headers = {'referer': get_referer(illust_id)}
    illust = requests.get(api_url, params=get_illust_params(illust_id)).text
    illust_json = json.loads(illust)
    name = illust_json['illust']['title']
    for errstr in name:
        if errstr in err_strList:
            index = err_strList.index(errstr)
            name = name.replace(errstr, re_strList[index])

    if illust_json['illust']['meta_single_page']:
        img_original = illust_json['illust']['meta_single_page']['original_image_url']
    else:
        img_original = illust_json['illust']['meta_pages'][0]['image_urls']['original']
    Picture_format = img_original[-4:]
    down_path = os.path.join(down_path, name + Picture_format)
    data = requests.get(img_original, headers=headers).content
    with open(down_path, 'wb') as f:
        f.write(data)
        print(name + '  下载完成！')