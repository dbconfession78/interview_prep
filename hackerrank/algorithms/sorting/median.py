import sys
import cProfile
from sort.merge_sort import merge_sort


def main():
    n = int(input())
    arr = [int(x) for x in input().strip().split(' ')]

    # test cases
    # arr = [0, 1, 2, 4, 8, 6, 5, 3]
    # arr = [1,2]
    print(median(arr))


def median(list):
    if len(list) % 2 == 0:
        merged = merge_sort(list)
        mid = int(len(merged) / 2) - 1
        avg = int(sum(merged[mid:mid+2]) / 2)
        return avg
    else:
        return merge_sort(list)[int(len(list) / 2)]


if __name__ == '__main__':
    main()
    # cProfile.run('main()')
