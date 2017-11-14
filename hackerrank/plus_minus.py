#!/usr/bin/python3

import sys

# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

n = 6
arr = [int(arr_temp) for arr_temp in '-4 3 -9 0 4 1'.strip().split(' ')]
pos = 0
neg = 0
zer = 0
for elem in arr:
    if elem > 0:
        pos += 1;
    elif elem < 0:
        neg += 1
    else:
        zer += 1

x = '%.6f' % (pos / n)
y = '%.6f' % (neg / n)
z = '%.6f' % (zer / n)
print('{}\n{}\n{}'.format(x, y, z))
