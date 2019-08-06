import time
from io import BytesIO

import pygame


def play():
    global audio_bytes
    audio_bytes = audio_bytes
    if audio_bytes is None:
        return
    byte_obj = BytesIO()
    byte_obj.write(audio_bytes)
    byte_obj.seek(0, 0)
    pygame.mixer.init()
    print(byte_obj)
    pygame.mixer.music.load(r"my_music/333.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == 1:
        time.sleep(0.1)
    pygame.mixer.music.stop()


def read_bytes(fn):
    with open(fn, 'rb') as fp:
        data = fp.read()
        # print(data)
    return data


if __name__ == '__main__':
    audio_bytes = read_bytes(r"my_music/222.mp3")
    pygame.mixer.init()
    play()