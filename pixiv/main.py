from pixiv.download import *
from pixiv.config import *

import argparse

load_config()

def main():
    parser = argparse.ArgumentParser(description='Welcome to ATDownloader!')
    parser.add_argument('-i', metavar='illust_id', dest='illust_id', help="作品ID", type=str)
    parser.add_argument('-is', metavar='illust_ids', dest='illust_ids', help="多个作品ID", nargs='*', type=str)
    parser.add_argument('-r', metavar='rank', dest='rank', help="排行榜，默认参数（mode=day，page=1，date='')", nargs=3, type=str)
    args = parser.parse_args()
    try:
        if args.illust_id:
            download_img_original(args.illust_id, IMG_DOWNLOAD_PATH)
        elif args.illust_ids:
            for illust_id in args.illust_ids:
                download_img_original(illust_id, IMG_DOWNLOAD_PATH)
        elif args.rank:
            if args.rank[0] == '_':
                args.rank[0] = 'day'
            if args.rank[1] == '_':
                args.rank[1] == '1'
            if args.rank[2] == '_':
                args.rank[2] = ''
            rank_download(RANK_DOWNLOAD_PATH, mode=args.rank[0], page=args.rank[1], date=args.rank[2])
    except Exception as e:
        print("发生错误：" + repr(e))

if __name__ == '__main__':
    main()

