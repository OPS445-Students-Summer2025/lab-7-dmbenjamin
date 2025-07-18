#!/usr/bin/env python3
# Student ID: dmbenjamin

class Time:
    """
    Object representing a clock time on a 24-hour scale.
    Data attributes: hour (0-23), minute (0-59), second (0-59)
    """
    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        # Basic type/range checking keeps bad values out at construction time
        if not (0 <= hour   < 24 and
                0 <= minute < 60 and
                0 <= second < 60):
            raise ValueError("Time values must satisfy 0≤h<24, 0≤m<60, 0≤s<60")
        self.hour   = hour
        self.minute = minute
        self.second = second

def format_time(t: Time) -> str:
    """
    Return *t* as zero-padded text in the form 'HH:MM:SS'.
    """
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"


def sum_times(t1: Time, t2: Time) -> Time:
    """
    Add two Time objects and return **normalised** result.

    Normalisation:
    • Seconds that reach 60 are converted to minutes.
    • Minutes that reach 60 are converted to hours.
    • Hours wrap around modulo 24 (08 + 17 → 01).
    """
    # Step 1 – raw addition
    s = Time()
    s.hour   = t1.hour   + t2.hour
    s.minute = t1.minute + t2.minute
    s.second = t1.second + t2.second

    # Step 2 – carry seconds → minutes
    if s.second >= 60:
        s.minute += s.second // 60
        s.second %= 60

    # Step 3 – carry minutes → hours
    if s.minute >= 60:
        s.hour  += s.minute // 60
        s.minute %= 60

    # Step 4 – wrap hours into 0-23
    s.hour %= 24

    return s


def valid_time(t: Time) -> bool:
    """
    Return True iff *t* contains a legal clock time.
    """
    return (
        0 <= t.hour   < 24 and
        0 <= t.minute < 60 and
        0 <= t.second < 60
    )