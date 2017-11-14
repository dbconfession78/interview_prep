#!/usr/bin/python3
import sys
"""
3
11 2 4
4 5 6
10 8 -12
"""
def diag_diff(a):
    i = 0
    sum1 = 0
    sum2 = 0

    for arr in a:
        sum1 += arr[i]
        i += 1

    i = 0
    for arr in a:
        sum2 += arr[n-i-1]
        i += 1
    print(abs(sum1 - sum2))

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
diag_diff(a)
