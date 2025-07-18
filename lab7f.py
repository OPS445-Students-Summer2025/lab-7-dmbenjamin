#!/usr/bin/env python3
# Student ID: dmbenjamin 
class Time:
    """Time of day (24-hour clock)."""

    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        self.hour, self.minute, self.second = hour, minute, second

    # ── printable forms ──────────────────────────────────────────
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def __repr__(self):
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"

    # ── operator overloading  (+)  ──────────────────────────────
    def __add__(self, other):
        """Enable  t1 + t2  for Time objects."""
        if isinstance(other, Time):
            return self.sum_times(other)
        return NotImplemented              # let Python try reversed op

    # ── existing helpers / methods ──────────────────────────────
    def format_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def sum_times(self, other):
        return sec_to_time(self.time_to_sec() + other.time_to_sec())


# ── standalone helper (unchanged) ───────────────────────────────
def sec_to_time(seconds):
    seconds %= 86_400
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)


def sec_to_time(seconds: int) -> Time:
    seconds %= 86_400
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)