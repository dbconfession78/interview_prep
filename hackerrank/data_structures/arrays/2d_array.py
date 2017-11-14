#!/usr/bin/python3
import sys

def sum_hourglass(arr, x, y):
    if y == 0 or y == len(arr)-1 or x > 3:
        return
#    print('[{}][{}]: {}'.format(x, y, arr[x][y]))
    top_left = arr[x][y-1]
    top_right = arr[x][y+1]
    center = arr[x+1][y]
    base = arr[x+2][y]
    base_left = arr[x+2][y-1]
    base_right = arr[x+2][y+1]

    _sum = top_left + arr[x][y] + top_right + center + base + base_left + base_right

    return _sum


def main():
    arr = []
    hg_dicts = []
    flag = False
    _max = None
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            hg_sum = sum_hourglass(arr, i, j)
            #                print('hg_sum [{}][{}]: {}'.format(i, j, hg_sum))
            if hg_sum is not None:
                if _max is not None:
                    if hg_sum > _max:
                        _max = hg_sum
                else:
                    _max = hg_sum
    print(_max)

if __name__ == '__main__':
    main()
