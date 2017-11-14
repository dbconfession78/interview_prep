#!/usr/bin/python3
import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum = 0
    for num in ar:
        sum += num
    return sum

n = 5
string = "1000000001 1000000002 1000000003 1000000004 1000000005"
ar = list(map(int, string.strip().split(' ')))
print(len(str(ar[0])))
result = aVeryBigSum(n, ar)
print(len(str(int(result))))
print(result)
