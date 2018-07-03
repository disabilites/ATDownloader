from configparser import ConfigParser
import os

BIT_RATE = '320000'
CONFIG_MAIN_PATH = os.path.join(os.path.expanduser('~'), '.ATDownloader')
CONFIG_FILE_PATH = os.path.join(CONFIG_MAIN_PATH, 'config.ini')
DEFAULT_DOWNLOAD_PATH = os.path.join(CONFIG_MAIN_PATH, 'ncm')
SONG_DOWNLOAD_PATH = os.path.join(DEFAULT_DOWNLOAD_PATH, 'song')
PLAYLIST_DOWNLOAD_PATH = os.path.join(DEFAULT_DOWNLOAD_PATH, 'playlist')
ALBUM_DOWNLOAD_PATH = os.path.join(DEFAULT_DOWNLOAD_PATH, 'album')

def load_config():
    if not os.path.exists(CONFIG_MAIN_PATH):
        init_config_file(CONFIG_MAIN_PATH)
    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    global BIT_RATE
    global SONG_DOWNLOAD_PATH
    global PLAYLIST_DOWNLOAD_PATH
    global ALBUM_DOWNLOAD_PATH

    BIT_RATE = config.get('ncm', 'br')
    SONG_DOWNLOAD_PATH = config.get('ncm', 'song_down_path')
    PLAYLIST_DOWNLOAD_PATH = config.get('ncm', 'playlist_down_path')
    ALBUM_DOWNLOAD_PATH = config.get('ncm', 'album_down_path')

def init_config_file(path):
    os.makedirs(path)

    default_config = '[ncm]\n' \
                     ';歌曲码率，可用值为 64000,128000,198000,320000\n'\
                     'br=320000\n'\
                     ';默认单曲下载路径\n'\
                     'song_down_path=' + DEFAULT_DOWNLOAD_PATH + '\song\n'\
                     ';默认歌单下载路径\n'\
                     'playlist_down_path=' + DEFAULT_DOWNLOAD_PATH + '\playlist\n'\
                     ';默认专辑下载路径\n'\
                     'album_down_path=' + DEFAULT_DOWNLOAD_PATH + '\\album\n'\

    with open(CONFIG_FILE_PATH, 'a') as f:
        f.write(default_config)
