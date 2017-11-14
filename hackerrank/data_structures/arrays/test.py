#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n, inputs = [int(n) for n in input().split(" ")]
    list = [0]*(n+1)
    for _ in range(inputs):
        x, y, incr = [int(n) for n in input().split(" ")]
        list[x-1] += incr
        if((y)<=len(list)): list[y] -= incr;
        input(list)
    max = x = 0
    print('x: {}'.format(x))
    for i in list:
        input('i: {}'.format(i))
        x=x+i;
        if(max<x): max=x;
    print(max)
