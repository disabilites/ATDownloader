from pixiv.constants import *
from pixiv.config import *

import requests
import json
import re

def illegal_string_replace(string):
    for errstr in string:
        if errstr in err_strList:
            index = err_strList.index(errstr)
            string = string.replace(errstr, re_strList[index])
    return string

def download_img_original(illust_id, down_path):
    headers = {'referer': get_referer(illust_id)}
    illust = requests.get(api_url, params=get_illust_params(illust_id)).text
    illust_json = json.loads(illust)
    name = illust_json['illust']['title']
    name = illegal_string_replace(name)

    if illust_json['illust']['meta_single_page']:
        img_original = illust_json['illust']['meta_single_page']['original_image_url']
    else:
        img_original = illust_json['illust']['meta_pages'][0]['image_urls']['original']
    picture_format = img_original[-4:]
    down_path = os.path.join(down_path, name + picture_format)
    data = requests.get(img_original, headers=headers).content
    with open(down_path, 'wb') as f:
        f.write(data)
        print(name + '  下载完成！')

def rank_download(down_path, mode='day', page='1', date=''):
    try:
        rank = requests.get(api_url, params=get_rank_params(mode, page, date)).text
        rank_json = json.loads(rank)
        rank_time = re.search('date=(.*)', rank_json['next_url']).group(1)
        down_path = os.path.join(down_path, mode, rank_time)
        if not os.path.exists(down_path):
            os.makedirs(down_path)
            print('创建成功！')

        illusts_len = len(rank_json['illusts'])
        for index in range(0, illusts_len):
            meta_pages = len(rank_json['illusts'][index]['meta_pages'])
            id = str(rank_json['illusts'][index]['id'])
            name = rank_json['illusts'][index]['title']
            name = illegal_string_replace(name)
            headers = {'referer': get_referer(id)}

            if not meta_pages:
                img_original = rank_json['illusts'][index]['meta_single_page']['original_image_url']
                picture_format = img_original[-4:]
                if os.path.join(down_path, name + picture_format):
                    data = requests.get(img_original, headers=headers).content
                    with open(os.path.join(down_path, name + picture_format), 'wb') as f:
                        f.write(data)
                        print(name + '  下载完成！')
                else:
                    print(name + '  已下载！')
            else:
                for meta_page in range(0, meta_pages):
                    img_original = rank_json['illusts'][index]['meta_pages'][meta_page]['image_urls']['original']
                    picture_format = img_original[-4:]
                    if not os.path.exists(os.path.join(down_path, name, name + '_' + str(meta_page) + picture_format)):
                        data = requests.get(img_original, headers=headers).content
                        if not os.path.exists(os.path.join(down_path, name)):
                            os.makedirs(os.path.join(down_path, name))
                        with open(os.path.join(down_path, name, name + '_' + str(meta_page) + picture_format), 'wb') as f:
                            f.write(data)
                            print(name + '_' + str(meta_page) + '  下载完成！')
                    else:
                        print(name + '_' + str(meta_page) + '  已下载！')
    except Exception:
        print('本日榜单尚未更新，请稍后再试！')