#!/usr/bin/env python3
# Student ID: dmbenjamin 
class Time:
    """Time of day (24-hour clock)."""
    def __init__(self, hour: int = 12, minute: int = 0, second: int = 0):
        # Just store what we’re given; validity is checked by valid_time()
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    def __str__(self) -> str:          # called by print()
        return self.format_time()

    __repr__ = __str__                 # so the REPL shows the same string


    def format_time(self) -> str:
        """Return self as 'HH:MM:SS'."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self) -> int:
        """Seconds since 00:00:00."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self) -> bool:
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

   
    def change_time(self, seconds: int) -> None:
        """In-place add (or subtract) seconds."""
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def sum_times(self, other: "Time") -> "Time":
        """Return a NEW Time = self + other (pure, does NOT mutate)."""
        return sec_to_time(self.time_to_sec() + other.time_to_sec())



def sec_to_time(seconds: int) -> Time:
    """Convert absolute seconds (mod 86 400) → Time object."""
    seconds %= 86_400
    minutes, sec = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, sec)