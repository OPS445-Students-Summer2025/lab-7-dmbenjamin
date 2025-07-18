#!/usr/bin/env python3
# Student ID: dmbenjamin

def function1():
    global schoolName          # modify the global variable, not a local copy
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName          # also works on the same global name
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

# ── main script ────────────────────────────────────────────────────
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)