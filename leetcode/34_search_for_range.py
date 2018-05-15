"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        l = 0
        r = len(nums) - 1
        while (l < r):
            m = (l + r) // 2
            v = nums[m]
            if v == target:
                l = m
                r = m
                while r < len(nums)-1 and nums[r+1] == target:
                    r += 1
                while l > 0 and nums[l-1] == target:
                    l -= 1
                return [l, r]
            elif v >= target:
                r = m
            else:
                l = m + 1
        if l == len(nums)-1:
            if nums[l] == target:
                return [l, l]
        if r == 0:
            if nums[r] == target:
                return [0, 0]
        return [-1, -1]



def main():
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print(Solution().searchRange([8, 8, 8, 8, 8, 8], 8))    # [0, 5]
    print(Solution().searchRange([8], 8))                   # [0, 0]
    print(Solution().searchRange([8, 8], 8))                # [0, 1]
    print(Solution().searchRange([0], 8))                   # [-1, -1]]
    print(Solution().searchRange([2,2], 3))                 # [-1, -1]]
    print(Solution().searchRange([1,4], 4))                 # [1, 1]]

#LC Input
# [5, 7, 7, 8, 8, 10]
# 8
# [8, 8, 8, 8, 8, 8]
# 8
# [8]
# 8
# [8,8]
# 8
# [2,2]
# 3
# [1,4]
# 4
if __name__ == '__main__':
    main()