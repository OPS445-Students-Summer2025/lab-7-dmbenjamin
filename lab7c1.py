#!/usr/bin/env python3
# Student ID: dmbenjamin

from lab7c import *

t1 = Time(8,  0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

td = Time(0, 50, 0)      # 50-minute delta

tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
change_time(t3, 1800)    # add 1 800 s (30 min) in-place

ft = format_time
print(f"{ft(t1)} + {ft(td)} --> {ft(tsum1)}")
print(f"{ft(t2)} + {ft(td)} --> {ft(tsum2)}")
print(f"09:50:00 + 1800 sec --> {ft(t3)}")