from ncm import config

api_url = 'https://api.imjad.cn/cloudmusic/'
err_strList = ['/', '\\', '<', '>', '|', ':', '?', '*', '"']
re_strList = ['／', '＼', '〈', '〉', '｜', '：', '？', '﹡', '“']

def get_song_params(song_id):
    song_params = {'type': 'song', 'id': song_id, 'br': config.BIT_RATE}
    return song_params

def get_detail_params(song_id):
    detail_params = {'type': 'detail', 'id': song_id}
    return detail_params

def get_playlist_params(playlist_id):
    playlist_params = {'type': 'playlist', 'id': playlist_id}
    return playlist_params
