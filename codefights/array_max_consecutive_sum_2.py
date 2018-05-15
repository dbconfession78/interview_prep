"""
210,247
CLOSE
PREV
NEXT
Description
My solutions
Leaderboard
Comments
Readme
CODEWRITING
SCORE: 300/300

Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.integer inputArray

    An array of integers.

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 105,
    -1000 ≤ inputArray[i] ≤ 1000.

    [output] integer

    The maximum possible sum of a subarray within inputArray.

"""
from sgk_test import test
# def arrayMaxConsecutiveSum2_PRACTICE(inputArray):
def arrayMaxConsecutiveSum2(inputArray):
    return

def arrayMaxConsecutiveSum2_PASSED(inputArray):
# def arrayMaxConsecutiveSum2(inputArray):
    loc_max = inputArray[0]
    glob_max = inputArray[0]
    prev_loc_max = [loc_max]
    for i in range(1, len(inputArray)):
        curr = inputArray[i]
        combo = curr + prev_loc_max[-1]
        loc_max = max(curr, combo)
        glob_max = max(glob_max, loc_max)
        prev_loc_max.append(loc_max)
        i += 1
    return glob_max

def main():
    ######### TESTS ############
    test(7, arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]))
    test(-1, arrayMaxConsecutiveSum2([-3, -2, -1, -4]))
    test(3, arrayMaxConsecutiveSum2([-3, 2, 1, -4]))
    test(8, arrayMaxConsecutiveSum2([1, -2, 3, -4, 5, -3, 2, 2, 2]))
    test(14, arrayMaxConsecutiveSum2([11, -2, 1, -4, 5, -3, 2, 2, 2]))
    test(1069, arrayMaxConsecutiveSum2([89, 96, 60, 10, 24, 30, 72, 40, 74, 49, 38, 87, 55, 46, 44, 14, 49, 88, 93, 11]))

if __name__ == "__main__":
    main()

