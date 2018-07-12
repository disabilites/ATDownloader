from htkt.hitokoto import *

import argparse

def main():
    parser = argparse.ArgumentParser(description='Welcome to ATDownloader!')
    parser.add_argument('-cat', metavar='cat', dest='cat', help="分类", nargs='?', type=str)
    args = parser.parse_args()
    try:
        if args.cat:
            get_hitokoto(cat=args.cat)
        else:
            get_hitokoto()
    except Exception as e:
        print("发生错误：" + repr(e))

if __name__ == '__main__':
    main()