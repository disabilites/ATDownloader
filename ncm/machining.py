from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, APIC, TPE1, TIT2, TALB, error

import requests

def add_metadata_to_song(file_path, songinfoDict):
    data = requests.get(songinfoDict['cover']).content
    try:
        audio = MP3(file_path, ID3=ID3)
    except HeaderNotFoundError:
        print('Can\'t sync to MPEG frame, not an validate MP3 file!')
        return

    if audio.tags is None:
        print('No ID3 tag, trying to add one!')
        try:
            audio.add_tags()
            audio.save()
        except error as e:
            print('Error occur when add tags:', str(e))
            return

    id3 = ID3(file_path)

    if id3.getall('APIC'):
        id3.delall('APIC')

    id3.add(
        APIC(
            encoding=0,
            mime='image/jpeg',
            type=3,
            data=data
        )
    )

    id3.add(
        TPE1(
            encoding=3,
            text=songinfoDict['artist']
        )
    )

    id3.add(
        TIT2(
            encoding=3,
            text=songinfoDict['name']
        )
    )

    id3.add(
        TALB(
            encoding=3,
            text=songinfoDict['album']
        )
    )

    id3.save(v2_version=3)