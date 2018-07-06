from configparser import ConfigParser
import os

CONFIG_MAIN_PATH = os.path.join(os.path.expanduser('~'), '.ATDownloader')
CONFIG_FILE_PATH = os.path.join(CONFIG_MAIN_PATH, 'config.ini')
DEFAULT_DOWNLOAD_PATH = os.path.join(CONFIG_MAIN_PATH, 'pixiv')
IMG_DOWNLOAD_PATH = os.path.join(DEFAULT_DOWNLOAD_PATH, 'img')
RANK_DOWNLOAD_PATH = os.path.join(DEFAULT_DOWNLOAD_PATH, 'rank')

def load_config():
    if not os.path.exists(CONFIG_MAIN_PATH):
        os.makedirs(CONFIG_MAIN_PATH)

    config = ConfigParser()
    config.read(CONFIG_FILE_PATH)

    if 'pixiv' not in config.sections():
        init_config_file()

    config.read(CONFIG_FILE_PATH)

    global IMG_DOWNLOAD_PATH
    global RANK_DOWNLOAD_PATH

    IMG_DOWNLOAD_PATH = config.get('pixiv', 'img_down_path')
    RANK_DOWNLOAD_PATH = config.get('pixiv', 'rank_down_path')

def init_config_file():
    default_config = '[pixiv]\n' \
                     ';默认图片下载路径\n'\
                     'img_down_path=' + IMG_DOWNLOAD_PATH + '\n'\
                     ';默认排行榜下载路径\n'\
                     'rank_down_path=' + RANK_DOWNLOAD_PATH + '\n'\

    with open(CONFIG_FILE_PATH, 'a') as f:
        f.write(default_config)

if __name__ == '__main__':
    load_config()