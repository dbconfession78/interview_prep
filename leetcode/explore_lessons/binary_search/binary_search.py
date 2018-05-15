"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        _len = len(nums)
        l = 0
        r = _len - 1

        while l <=r:
            m = l + (r - l) // 2
            val = nums[m]
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return -1



def main():
    print(Solution().search([-1,0,3,5,9,12], 9))
    print(Solution().search([1,2], 1))
    print(Solution().search([1,2], 2))
    print(Solution().search([-1,0,3,5,9,12], 2))  # -1


#LC Input

# [-1,0,3,5,9,12]
# 9
# [1,2]
# 1
# [1,2]
# 2
if __name__ == '__main__':
    main()