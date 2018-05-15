from random import random, choice
'''
Given: sorted array of integers
Return: sorted array of squares of those integers
Ex: [-1,3,5] -> [1,9,25]
Integers can be negative.
'''

from bisect import bisect
# def get_squares_PRACTICE(arr):
def get_squares(arr):
    retlst = []
    for i, num in enumerate(arr):
        retlst.insert(bisect(retlst, (num)**2), (num)**2)
    return retlst

def get_squares_MINE(arr):
# def get_squares(arr):
    ret_arr = []
    for elem in arr:
        ret_arr.append(abs(elem * elem))
    return merge_sort(ret_arr)


def merge_sort(arr):
    i = j = k = 0

    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    # recursively break each side
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    while i < len(L) and j < len(R):
        if L[i] >= R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


def main():
    print(get_squares([-1,3,5]))
    # arr = []
    # for i in range(10000):
    #     _i = i
    #     arr.append(choice(range(-10,10)))
    # print(get_squares(arr))

if __name__ == "__main__":
    main()



"""
def main():
    func()


def func():
    return


if __name__ == '__main__':
    main()

"""