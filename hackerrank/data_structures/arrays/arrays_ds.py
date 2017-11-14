#!/usr/bin/python3
import sys
n = 4
ar = [1, 4, 3, 2]




for i in range(1, len(ar)+1):
    sys.stdout.write('{}'.format(ar[-i]))
    if i != len(ar):
        sys.stdout.write(' ')
    else:
        print()
