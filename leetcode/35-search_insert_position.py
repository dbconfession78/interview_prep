# Instructions
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6]
5
Output: 2
Example 2:

Input: [1,3,5,6]
2
Output: 1
Example 3:

Input: [1,3,5,6]
7
Output: 4
Example 1:

Input: [1,3,5,6]
0
Output: 0

"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        _len = len(nums)
        if target == nums[_len-1]:
            return _len-1
        if target <= nums[0]:
            return 0
        if target > nums[_len-1]:
            return _len
        l = 0
        r = _len - 1
        while l <= r:
            mid_i = l + (r - l) // 2
            mid_val = nums[mid_i]

            if nums[mid_i+1] > target > mid_val:
                return mid_i + 1

            if nums[mid_i-1] < target < mid_val:
                return mid_i

            if mid_val == target:
                return mid_i
            if mid_val < target:
                l = mid_i
            if mid_val > target:
                r = mid_i

# start -> debug: 39 min
# debug to pass: +2 hr 52 mins
def main():
    print(Solution().searchInsert([1,3,5,6],5))            # 2
    print(Solution().searchInsert([1,4,6,8,9], 7))          # 3
    print(Solution().searchInsert([1,4,6,8,9], 5))          # 2
    print(Solution().searchInsert([1, 3, 5, 6], 7))         # 4
    print(Solution().searchInsert([1], 1))                  # 0
    print(Solution().searchInsert([5], 4))                  # 0
    print(Solution().searchInsert([5], 6))                  # 1
    print(Solution().searchInsert([1, 3, 5, 6], 2))         # 1
    print(Solution().searchInsert([1, 3, 5, 6], 0))         # 0
    print(Solution().searchInsert([1, 3], 2))               # 1
    print(Solution().searchInsert([1, 3, 5], 4))            # 2
    print(Solution().searchInsert([3, 4, 5, 6, 7, 8], 6))   # 3
    print(Solution().searchInsert([1, 3, 5], 5))            # 2




# LC input
# [1,3,5,6]
# 5
# [1,4,6,8,9]
# 7
# [1,4,6,8,9]
# 5
# [1,3,5,6]
# 7
# [1]
# 1
# [5]
# 4
# [5]
# 6
# [1,3,5,6]
# 2
# [1,3,5,6]
# 0
# [1,3]
# 2
# [1,3,5]
# 4
# [3,4,5,6,7,8]
# 6
# [1,3,5]
# 5

if __name__ == '__main__':
    main()

"""
--


def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""