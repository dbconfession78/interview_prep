#!/bin/python3

import sys
from sort.merge_sort import merge_sort
from sort.insertion_sort_pt2 import Sort


def main():
    n = int(input().strip())
    a = []
    a_i = 0
    for a_i in range(n):
       a_t = int(input().strip())
       a.append(a_t)

    # a = [12, 4, 5, 3, 8, 7]

    heap = []
    i = 0
    for _ in range(n):
    #while i < len(a):
        # heap.append(a[i])
        heap = Sort().insertion_sort(a)
        print(float(get_median(heap, len(heap))))
        i += 1



def get_median(heap, size):
    meidan = 0
    if size % 2 == 0:
        x = heap[size // 2]
        y = heap[(size // 2) - 1]
        median = (x + y) / 2
    else:
        median = heap[size // 2]

    print('%.1f' % median)
    return (median)


if __name__ == '__main__':
    main()
    # cProfile.run('main()')