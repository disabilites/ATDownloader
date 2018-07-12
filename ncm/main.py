from ncm.download import *
from ncm.config import *

import argparse

load_config()

def main():
    parser = argparse.ArgumentParser(description='Welcome to ATDownloader!')
    parser.add_argument('-s', metavar='song_id', dest='song_id', help="歌曲ID", type=str)
    parser.add_argument('-ss', metavar='song_ids', dest='song_ids', help="多首歌曲ID", nargs='*', type=str)
    parser.add_argument('-p', metavar='playlist_id', dest='playlist_id', help="歌单ID", type=str)
    parser.add_argument('-a', metavar='album_id', dest='album_id', help="专辑ID", type=str)
    args = parser.parse_args()
    try:
        if args.song_id:
            song_download(get_song_info(args.song_id), path=SONG_DOWNLOAD_PATH)
        elif args.song_ids:
            for song_id in args.song_ids:
                song_download(get_song_info(song_id), path=SONG_DOWNLOAD_PATH)
        elif args.playlist_id:
            playlist_download(args.playlist_id, path=PLAYLIST_DOWNLOAD_PATH)
        elif args.album_id:
            album_download(args.album_id, path=ALBUM_DOWNLOAD_PATH)
    except Exception as err:
        print("发生错误：" + repr(err))

if __name__ == '__main__':
    main()

