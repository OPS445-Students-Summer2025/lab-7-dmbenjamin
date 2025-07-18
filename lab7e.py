#!/usr/bin/env python3
# Student ID: dmbenjamin 
class Time:
    """Time of day (24-hour clock)."""

    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        # Store whatever is given; valid_time() can check the range later.
        self.hour, self.minute, self.second = hour, minute, second

    
    def __str__(self) -> str:          # used by print()
        return self.format_time()      # HH:MM:SS with colons

    def __repr__(self) -> str:         # shown at the REPL
        return f"{self.hour:02d}.{self.minute:02d}.{self.second:02d}"  # dots

    
    def format_time(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self) -> int:
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self) -> bool:
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    
    def change_time(self, seconds: int) -> None:
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def sum_times(self, other: "Time") -> "Time":
        return sec_to_time(self.time_to_sec() + other.time_to_sec())



def sec_to_time(seconds: int) -> Time:
    seconds %= 86_400
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)