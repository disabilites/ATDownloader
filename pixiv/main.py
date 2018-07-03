from pixiv.download import *
from pixiv.config import *

import argparse

load_config()

def main():
    parser = argparse.ArgumentParser(description='Welcome to ATDownloader!')
    parser.add_argument('-i', metavar='illust_id', dest='illust_id', help='illust_id', type=str)
    args = parser.parse_args()
    try:
        if args.illust_id:
            download_img_original(args.illust_id, IMG_DOWNLOAD_PATH)
    except Exception:
        print('ID错误！')

if __name__ == '__main__':
    main()

