# Instructions
"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from sgk_test import test
class Solution(object):
    # def productExceptSelf_PRACTICE(self, nums):
    def productExceptSelf(self, nums):
        zero_count = 0
        prod = 1
        for num in nums:
            if num != 0:
                prod *= num
            else:
                if zero_count == 1:
                    return [0 for _ in range(len(nums))]
                zero_count += 1

        return [prod if x == 0 else 0 for x in nums] if zero_count > 0 else [prod // x for x in nums]


    def productExceptSelf_PASSED(self, nums):
    # def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output



def main():
    test([0, 0], Solution().productExceptSelf([0, 0]))           # [0, 0]
    test([24,12,8,6], Solution().productExceptSelf([1, 2, 3, 4]))     # [24,12,8,6]
    test([24,0,0,0,0], Solution().productExceptSelf([0, 1, 2, 3, 4]))  # [24,0,0,0,0]
    test([0,0,0,0,0], Solution().productExceptSelf([0, 1, 0, 3, 4]))  # [0,0,0,0,0]
    test([0, 1], Solution().productExceptSelf([1, 0]))           # [0,1]


# LC input
# [0, 0]
# [1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 0, 3, 4]
# [1, 0]

if __name__ == '__main__':
    main()