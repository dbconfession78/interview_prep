#!/usr/bin/python3
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key

m = 6
#m = int(input().strip())
ar = '4 1 3 5 6 2'
ar = [int(i) for i in ar.strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
