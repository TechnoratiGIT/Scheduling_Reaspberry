import subprocess
from pymediainfo import MediaInfo
import random

vlc_ = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"  # vlc player save location (Windows)


def get_clip_time(file: str):
    """
    :param file: location of file
    :return: length of (video or audio) file in seconds
    """
    duration_in_ms = MediaInfo.parse(file).tracks[0].duration
    return (duration_in_ms - duration_in_ms % 1000) / 1000


def play_file(file: (str, list), program: str = vlc_, play_time: int = 0):
    """
    Plays an audio or video file with the vlc player,
    if multiple files are given it chooses one randomly
    :param file: location of file or list of locations of multiple files
    :param program: program to play the file
    :param play_time: play time in seconds
    """
    """get a random file out of list"""
    if file is list:
        file = random.choice(file)
    """set the playtime"""
    full_time = get_clip_time(file)
    if full_time < play_time or play_time == 0:
        play_time = full_time
    print(play_time)
    """play the file"""
    subprocess.Popen([program, file, "--run-time=" + str(play_time), "vlc://quit"])


if __name__ == "__main__":
    pass  # put something in if you want

else:
    print("::::  imported play vid  ::::")
   
