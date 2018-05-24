from sgk_test import test
def flip(arr, k):  # arr: [1, 5, 4, 3, 2], k: 2
    i = 0
    j = k - 1
    while i < j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1


def pancake_sort(arr):
    i = 0
    j = 1
    _len = len(arr)
    x = 0
    while x < _len - 1:
        mx = max(arr[:_len - x])
        mx_idx = arr.index(mx)
        flip(arr, mx_idx + 1)
        flip(arr, _len - x)
        x += 1

    return arr



def main():
    ######### TESTS ############
    test([1,2,3,4,5], pancake_sort(([1, 5, 4, 3, 2])))

if __name__ == "__main__":
    main()

