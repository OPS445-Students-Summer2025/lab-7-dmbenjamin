#!/usr/bin/env python3
# Student ID: dmbenjamin

class Time:
    
    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        if not (0 <= hour   < 24 and
                0 <= minute < 60 and
                0 <= second < 60):
            raise ValueError("0 ≤ h<24, 0 ≤ m<60, 0 ≤ s<60 expected")
        self.hour   = hour
        self.minute = minute
        self.second = second

def format_time(t: Time) -> str:
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"


def sum_times(t1: Time, t2: Time) -> Time:
   
    total_seconds = (
        t1.hour   * 3600 + t1.minute * 60 + t1.second +
        t2.hour   * 3600 + t2.minute * 60 + t2.second
    ) % 86_400                      # keep inside one day

    return Time(
        total_seconds // 3600,
        (total_seconds % 3600) // 60,
        total_seconds % 60
    )


def valid_time(t: Time) -> bool:
   
    return (
        0 <= t.hour   < 24 and
        0 <= t.minute < 60 and
        0 <= t.second < 60
    )


def change_time(time: Time, seconds: int) -> None:
    
    # Convert current time → absolute seconds, apply delta, wrap to 0–86399
    total = (time.hour * 3600 + time.minute * 60 + time.second + seconds) % 86_400

    # Write the decomposed values back into the same object
    time.hour   = total // 3600
    time.minute = (total % 3600) // 60
    time.second = total % 60
    