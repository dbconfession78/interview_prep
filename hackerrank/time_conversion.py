#!/usr/bin/python3
# usage: ./time_conversion.py <HH:MM:SSP>
import sys

def timeConversion(s):
    # Complete this function
    s = s.split(':')
    am_pm = s[2][-2:]
    s[2] = s[2][:-2]
    if am_pm == 'PM':
        if int(s[0]) < 12:
            s[0] = str(int(s[0]) + 12)
    elif int(s[0]) == 12:
            s[0] = '00'
    return '{}:{}:{}'.format(s[0], s[1], s[2])


s = input().strip()
result = timeConversion(s)
print(result)
