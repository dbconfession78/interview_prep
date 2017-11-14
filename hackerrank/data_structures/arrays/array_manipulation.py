#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arr_s, num_lines = [int(x) for x in input().strip().split(' ')]
    arr = [0 for i in range(arr_s+1)]
    
    for _ in range(num_lines):
        a, b, k = [int(x) for x in input().strip().split(' ')]
        arr[a-1] += k
        arr[b] -= k

    max = 0
    x = 0
    for elem in arr:
        x += elem
        if max < x:
            max = x

    print(max)


