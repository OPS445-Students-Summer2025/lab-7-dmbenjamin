#!/usr/bin/env python3
# Student ID: dmbenjamin

class Time:
    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        if not (0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60):
            raise ValueError("Time values out of range")
        self.hour, self.minute, self.second = hour, minute, second


def format_time(t: Time) -> str:
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"


def time_to_sec(t: Time) -> int:
    return t.hour * 3600 + t.minute * 60 + t.second


def sec_to_time(seconds: int) -> Time:
    seconds %= 86_400                         # wrap into one day
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)


def sum_times(t1: Time, t2: Time) -> Time:
    return sec_to_time(time_to_sec(t1) + time_to_sec(t2))


def valid_time(t: Time) -> bool:
    return 0 <= t.hour < 24 and 0 <= t.minute < 60 and 0 <= t.second < 60


def change_time(t: Time, seconds: int) -> None:
    new = sec_to_time(time_to_sec(t) + seconds)
    t.hour, t.minute, t.second = new.hour, new.minute, new.second