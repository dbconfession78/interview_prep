import sys
import cProfile


def main():
    54321

    arr = [5, 4, 3, 2, 1]
    arr = []
    arr = [3, 2, 1]
    # arr = []
    a_len = len(arr)
    print('start: {}'.format(arr))
    swaps = bubble_sort(arr, a_len)
    print('sorted: {}'.format(arr))
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(arr[0] if a_len > 0 else ""))
    print('Last Element: {}'.format(arr[a_len-1] if a_len > 0 else ""))


def bubble_sort(arr, len):
    swaps = 0
    if len <= 1:
        return 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        i = 1
        while i < len:
            # if i > 0:
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                swaps += 1
                is_sorted = False
            i += 1

    return swaps





if __name__ == '__main__':
    main()
    # cProfile.run('main()')