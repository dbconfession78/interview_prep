#!/usr/bin/python3
from collections import deque
import sys

def leftRotation(a, d):
    dq = deque(a)
    for i in range(d):
        dq.rotate(-1)
    return dq

def leftRotation_manual(a, d):
    for i in range(d):
        temp = a[0]
        for j in range(len(a)-1):
            a[j] = a[j+1]
        a[len(a)-1] = temp 
    return a
    
    

if __name__ == "__main__":
 #   n, d = input().strip().split(' ')
 #   n, d = [int(n), int(d)]
#    a = list(map(int, input().strip().split(' ')))
#    result = leftRotation_bitshift(a, d)
    result = leftRotation(a, d)
    n = 5
    d = 6
    a = []
    for i in range(n):
        a.append(i)
    print(a)
    print()
    result1 = leftRotation_manual(a, d)
    a = []
    for i in range(n):
        a.append(i)

    result2 = leftRotation(a, d)
    print ("man: {}".format(" ".join(map(str, result1))))
    print ("lib: {}".format(" ".join(map(str, result2))))
    
