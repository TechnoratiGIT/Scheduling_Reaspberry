from schedule import functools
import schedule
import time
import play_vid
import json


def get_content(path):
    with open(path, "r") as f:
        content_string = f.read()
    return json.loads(content_string)


alarm_file = r"VID_AUD_FILES\Futon.mp4"


def print_jobs():
    print(schedule.get_jobs())
    print()


def play_video(file):
    close_id, wait_time = play_vid.play_file(file, buffer=1)
    schedule.every(wait_time).seconds.do(close_video_player, close_id)


def close_video_player(close_id):
    play_vid.terminate_file(close_id)
    return schedule.CancelJob


def schedule_jobs():
    schedule.every(5).seconds.do(print_jobs)
    schedule.every().day.at("06:30").do(play_video, alarm_file).tag("daily", "alarm")
    schedule.every().day.at("00:00:05").do(schedule_jobs_daily).tag("daily", "setup")


def schedule_jobs_daily():
    schedule.clear("once")
    t = str(schedule.datetime.datetime.now())
    print(t)
    jobs = get_content(r"schedule_over_the_year\once.json")
    print(jobs)
    try:
        day_jobs = jobs[t[0:4]][t[8:10] + "." + t[5:7]]
        for job in day_jobs:
            schedule.every().day.at(job["time"]).do(globals()[job["func"]], *job["arguments"]).tag(*job["tags"], "once")
    except KeyError:
        pass


if __name__ == "__main__":

    schedule_jobs()
    schedule_jobs_daily()

    while True:
        n = schedule.idle_seconds()
        if n is None:
            break
        elif n > 0:
            time.sleep(n)
        schedule.run_pending()
