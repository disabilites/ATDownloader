from ncm.constants import api_url
from ncm.constants import re_strList
from ncm.constants import err_strList
from ncm.constants import get_song_params
from ncm.constants import get_detail_params
from ncm.constants import get_playlist_params
from ncm.machining import add_metadata_to_song

import requests
import json
import os

def get_song_info(song_id):
    songinfoDict = {}
    song = requests.get(api_url, get_song_params(song_id)).text
    detail = requests.get(api_url, get_detail_params(song_id)).text
    song_json = json.loads(song)
    detail_json = json.loads(detail)
    songinfoDict['url'] = song_json['data'][0]['url']
    songinfoDict['name'] = detail_json['songs'][0]['name']
    try:
        if detail_json['songs'][0]['ar'][1]['name']:
            songinfoDict['artist'] = detail_json['songs'][0]['ar'][0]['name'] + '／' + detail_json['songs'][0]['ar'][1]['name']
    except IndexError:
        songinfoDict['artist'] = detail_json['songs'][0]['ar'][0]['name']
    songinfoDict['cover'] = detail_json['songs'][0]['al']['picUrl']
    songinfoDict['album'] = detail_json['songs'][0]['al']['name']
    return songinfoDict

def song_download(songinfoDict, down_path):
    if not os.path.exists(down_path):
        os.makedirs(down_path)
        print('ofk')
    name = songinfoDict['artist'] + ' - ' + songinfoDict['name']
    for errstr in name:
        if errstr in err_strList:
            index = err_strList.index(errstr)
            name = name.replace(errstr, re_strList[index])
    down_path = down_path + '\\' + name + '.mp3'

    song_data = requests.get(songinfoDict['url']).content
    with open(down_path, 'wb') as f:
        f.write(song_data)
        print('下载完成')
    add_metadata_to_song(down_path, songinfoDict)

def playlist_download(playlist_id, path):
    playlist = requests.get(api_url, get_playlist_params(playlist_id)).text
    playlist_json = json.loads(playlist)
    length = len(playlist_json['playlist']['tracks'])
    for i in range(0, length):
        song_download(get_song_info(playlist_json['playlist']['tracks'][i]['id']), path)