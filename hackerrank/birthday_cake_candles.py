#!/usr/bin/python3
import sys

def birthdayCakeCandles(n, ar):
    # Complete this function

    tallest = max(ar)
    count = ar.count(tallest)
    return count

n = 4
string = '3 4 5 5 5 4 3 2 5'
ar = list(map(int, string.strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
