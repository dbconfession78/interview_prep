# Instructions
"""
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest
nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value
an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you
can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading
off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4
"""
test_no = 1
# def get_different_number_PRACTICE(arr):
def get_different_number(arr):
    return

def get_different_number_DCT(arr):
# def get_different_number(arr):
    cache = [None for _ in range(len(arr))]
    for num in arr:
        if (num >= len(arr)):
            continue
        cache[num] = True

    i = 0
    while i < len(cache):
        if not cache[i]:
            return i
        i += 1

    return len(arr)

def get_different_number_SORT(arr):
# def get_different_number(arr):
    arr.sort()

    if len(arr) == 0:
        return 0
    i = 0
    while i < len(arr):
        n = arr[i]
        if n != i:
            return i
        i += 1
    return n + 1

def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))

def main():
    test(1, get_different_number([0]))                    # 1
    test(3, get_different_number([0, 1, 2]))              # 3
    test(4, get_different_number([1, 3, 0, 2, ]))         # 4
    test(0, get_different_number([100000]))               # 0
    test(2, get_different_number([1, 0, 3, 4, 5]))        # 2
    test(1, get_different_number([0, 99999, 100000]))     # 1


if __name__ == '__main__':
    main()
