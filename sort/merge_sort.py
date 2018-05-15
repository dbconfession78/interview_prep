import sys
import cProfile
from sort.quick_sort import quicksort_comp

def main():
    list = [7, 40, 33, 67, 3, 3453, 223]
    list = [1, 7, 3, 10, 4, 2, 5, 8, 6, 9]
    print(merge_sort(list))

# def merge_sort_PRACTICE(lst):
def merge_sort(lst):
    _len = len(lst)
    if _len < 2:
        return lst

    L = merge_sort(lst[:_len // 2])
    R = merge_sort(lst[_len // 2:])
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        lst[k] = L[i]
        i += 1; k += 1

    while j < len(R):
        lst[k] = R[j]
        j += 1; k += 1
    return lst


def merge_sort_PASSED(lst):
# def merge_sort(lst):
    if len(lst) >= 2:
        left = merge_sort(lst[:len(lst) // 2])
        right = merge_sort(lst[len(lst) // 2:])
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                lst[k] = right[j]
                j += 1
            else:
                lst[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst


if __name__ == '__main__':
    main()
