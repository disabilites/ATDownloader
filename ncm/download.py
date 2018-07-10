from bs4 import BeautifulSoup
from ncm.machining import add_metadata_to_song
from ncm.constants import *

import requests
import json
import os
import re

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
        print("目录创建成功！")
    name = songinfoDict['artist'] + ' - ' + songinfoDict['name']
    for errstr in name:
        if errstr in err_strList:
            index = err_strList.index(errstr)
            name = name.replace(errstr, re_strList[index])

    down_path = os.path.join(down_path, name + '.mp3')
    if not os.path.exists(down_path):
        song_data = requests.get(songinfoDict['url'], stream=True)
        length = int(song_data.headers.get('Content-Length'))
        progress = ProgressBar(down_path, length)
        with open(down_path, 'wb') as f:
            for buffer in song_data.iter_content(chunk_size=1024):
                if buffer:
                    f.write(buffer)
                    progress.refresh(len(buffer))
        add_metadata_to_song(down_path, songinfoDict)
    else:
        print(name + "已存在！")

def playlist_download(playlist_id, path):
    playlist_url = 'https://music.163.com/playlist?id=' + playlist_id
    html = requests.get(playlist_url).text
    soup = BeautifulSoup(html, 'lxml')
    playlistname = re.match(r"(.*?) - 歌单 - 网易云音乐", soup.title.string).group(1)
    path = path + '\\' + playlistname
    playlist = requests.get(api_url, get_playlist_params(playlist_id)).text
    playlist_json = json.loads(playlist)
    playlist_len = len(playlist_json['playlist']['tracks'])
    for index in range(0, playlist_len):
        song_download(get_song_info(playlist_json['playlist']['tracks'][index]['id']), path)

def album_download(album_id, path):
    album = requests.get(api_url, get_album_params(album_id)).text
    album_json = json.loads(album)
    albumname = album_json['songs'][0]['al']['name']
    path = path + '\\' + albumname
    album_len = len(album_json['songs'])
    for index in range(0, album_len):
        song_download(get_song_info(album_json['songs'][index]['id']), path)

class ProgressBar(object):

    def __init__(self, file_name, total):
        super().__init__()
        self.file_name = file_name
        self.count = 0
        self.prev_count = 0
        self.total = total
        self.end_str = '\r'

    def __get_info(self):
        return 'Progress: {:6.2f}%, {:8.2f}KB, [{:.30}]'\
            .format(self.count/self.total*100, self.total/1024, self.file_name)

    def refresh(self, count):
        self.count += count
        if (self.count - self.prev_count) > 10240:
            self.prev_count = self.count
            print(self.__get_info(), end=self.end_str)
        if self.count >= self.total:
            self.end_str = '\n'
            print(self.__get_info(), end=self.end_str)