from ncm.download import get_song_info
from ncm.download import song_download
from ncm.download import playlist_download
from ncm.config import load_config
from ncm.config import SONG_DOWNLOAD_PATH
from ncm.config import PLAYLIST_DOWNLOAD_PATH

import argparse

load_config()

def main():
    parser = argparse.ArgumentParser(description='Welcome to ATDownloader!')
    parser.add_argument('-s', metavar='song_id', dest='song_id', help='song_id', type=str)
    parser.add_argument('-p', metavar='playlist_id', dest='playlist_id', help='playlist_id', type=str)
    args = parser.parse_args()
    try:
        if args.song_id:
            song_download(get_song_info(args.song_id), path=SONG_DOWNLOAD_PATH)
        elif args.playlist_id:
            playlist_download(args.playlist_id, path=PLAYLIST_DOWNLOAD_PATH)
    except Exception:
        print('ID错误！')

if __name__ == '__main__':
    main()

