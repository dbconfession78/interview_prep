"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3

Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


class Solution:
    # def triangleNumber_PRACTICE(self, nums):
    def triangleNumber(self, lst):
        retval = 0
        i = 0
        _len = len(lst)
        j = len(lst) - 1
        while i < j:
            j = len(lst) - 1
            k = i + 1
            while k < j:
                if lst[i] + lst[k + 1] > lst[j]:
                    retval += 1
                if lst[i] + lst[k] > lst[j - 1]:
                    retval += 1
                if lst[i] + lst[k] > lst[j]:
                    k += 1
                else:
                    j -= 1
            i += 1
        return retval
    def triangleNumber_PASSED(self, nums):
    # def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        retval = 0
        j = len(nums) - 1
        while i < j:
            j = len(nums) - 1
            k = i + 1
            while k < j:
                if nums[i] + nums[k+1] > nums[j]:
                    retval += 1
                if nums[i] + nums[k] > nums[j-1]:
                    retval += 1
                if nums[i] + nums[k] > nums[j]:
                    k += 1
                else:
                    j -= 1
            i += 1
        return retval






def main():
    print(Solution().triangleNumber([3, 4, 5, 6, 7, 8, 9])) #
    # print(Solution().triangleNumber([2,2,3,4]))     # 3
    # print(Solution().triangleNumber([1,1]))         # 0
    # print(Solution().triangleNumber([0,1,1,1]))     # 1


# LC input
# [2,2,3,4]
# [1,1]
# [0,1,1,1]

if __name__ == '__main__':
    main()