#!/usr/bin/python3
import sys

string = '1 2 3 4 5'
arr = list(map(int, string.strip().split(' ')))
sums = [sum(arr)-num for num in arr]
print('{} {}'.format(min(sums), max(sums)))
