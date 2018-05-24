"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

pseudo:
1) put the arrr into a set
2) starting from 0 check for the int in  set, returning the first not found
"""

from sgk_test import test
def find_first_missing_int(arr):
    if not arr:
        return None
    st = set(arr)
    mx = max(st)
    for i in range(1, mx+2):
        if i not in st:
            return i





def main():
    ######### TESTS ############
    test(2, find_first_missing_int([3, 4, -1, 1]))
    test(3, find_first_missing_int([1, 2, 0]))
    test(1, find_first_missing_int([0]))
    test(None, find_first_missing_int([]))

if __name__ == "__main__":
    main()

