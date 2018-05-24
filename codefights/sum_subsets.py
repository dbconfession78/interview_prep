"""
Given a sorted array of integers arr and an integer num, find all possible unique subsets of arr that add up to num.
Both the array of subsets and the subsets themselves should be sorted in lexicographical order.

Example

For arr = [1, 2, 3, 4, 5] and num = 5, the output should be
sumSubsets(arr, num) = [[1, 4], [2, 3], [5]].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

A sorted array of integers.

Guaranteed constraints:
0 ≤ arr.length ≤ 50,
1 ≤ arr[i] ≤ num.

[input] integer num

A non-negative integer.

Guaranteed constraints:
0 ≤ num ≤ 1000.

[output] array.array.integer

A sorted array containing sorted subsets composed of elements from arr that have a sum of num. It is guaranteed that
there are no more than 1000 subsets in the answer
"""

from sgk_test import test
def sumSubsets(arr, num):
    retval = []
    _len = len(arr)
    stk = [([arr[0]], 0, 0)]
    memo = set()
    while stk:
        lst, sm, j = stk.pop()
        i = 1

        while i < _len:
            if j != i:
                if sm + arr[i] == num:
                    x = sm + arr[i]
                    y = lst
                    if tuple(lst) not in memo:
                        retval.append(lst + [arr[i]])
                        memo.add(tuple(lst))
                elif (sm + arr[i]) < num:
                        stk.append((lst + [arr[i]], sm + arr[i], i))
                else:
                    break

            i += 1



def main():
    ######### TESTS ############
    # test([[1,4], [2,3], [5]], sumSubsets([1,2,3,4,5], 5))
    # test([[1,2,2], [1,4], [2,3], [5]], sumSubsets([1,2,2,3,4,5], 5))
    # test([[]], sumSubsets([], 0))
    # test([[1,1,1,1,1,1,1,1,1]], sumSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1], 9))

    test([[1,1,2,5],[1,2,6],[1,8],[2,2,5]], sumSubsets([1, 1, 2, 2, 2, 5, 5, 6, 8, 8], 9))
    # test([[1,2,2], [1,4], [2,3], [5]], sumSubsets([1,2,2,3,4,5], 5))


if __name__ == "__main__":
    main()

