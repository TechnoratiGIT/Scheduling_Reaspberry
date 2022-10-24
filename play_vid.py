import subprocess
import time
from pymediainfo import MediaInfo

vlc = r"C:\Program Files\VLC Plus Player\vlc.exe"


def get_clip_time(file: str):
    media_info = MediaInfo.parse(file)
    duration_in_ms = media_info.tracks[0].duration
    return (duration_in_ms - duration_in_ms % 1000) / 1000


def play_file(file: str, prog: str = vlc, play_time: int = 0, buffer: int = 0):
    if play_time == 0:
        play_time = get_clip_time(file)
        print(play_time)
    play = subprocess.Popen([prog, file])
    return play, play_time + buffer


def terminate_file(play_object):
    play_object.terminate()


def wait_play_time(time_):
    time.sleep(time_)


def test(text):
    print(text)


if __name__ == "__main__":
    # File (a CAD in this case) and Program (desired CAD software in this case) # r: raw strings
    futon = r"VID_AUD_FILES\Futon.mp4"
    info = play_file(futon, buffer=1)
    wait_play_time(info[1])
    terminate_file(info[0])
else:
    print("::::  imported play vid  ::::")
