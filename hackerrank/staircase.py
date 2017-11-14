#!/usr/bin/python3

n = 6

for i in range(n):
    print('{}{}'.format(' ' * (n-i-1), '#' * (i+1)))
