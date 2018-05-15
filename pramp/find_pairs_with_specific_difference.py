# Find Pairs with Specific Difference
"""
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

In your solution, try to reduce the memory usage while maintaining time efficiency. Prove the correctness of your solution and analyze its time and space complexities.

Note: the order of the pairs in the output array doesn’t matter.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[0, -1], [-1, -2], [2, 1], [1, 0]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        0 ≤ arr.length ≤ 100

    [input]integer k
        k ≥ 0

    [output] array.array.integer

"""
test_no = 1
def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))



# def find_pairs_with_given_difference_PRACTICE(self, arr, k):
def find_pairs_with_given_difference(arr, k):
    return 0

def find_pairs_with_given_difference_PASSED(arr, k):
# def find_pairs_with_given_difference(arr, k):
    j = 1
    i = 0
    retval = []
    arr.sort()
    while i < len(arr) and j < len(arr):
        s = abs(arr[i] - arr[j])
        if s == k and i != j:
            retval.append([arr[j], arr[i]])
            i += 1
        elif s > k:
            i += 1
        else:
            j += 1
    return retval


def main():
    test([[0, -1], [-1, -2], [2, 1], [1, 0]], find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
    test([[]], find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))
    test([[32, 5]], find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 27))
    test([[4, 1]], find_pairs_with_given_difference([4, 1], 3))



if __name__ == '__main__':
    main()