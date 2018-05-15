class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _len = len(nums)
        if _len == 0:
            return [-1, -1]
        if _len == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        mid_i = _len // 2
        mid_val = nums[mid_i]
        L = 0; R = _len - 1
        start = -1; end = -1
        while len(nums[L:R+1]) > 2:
            if mid_val == target:
                i = j = mid_i
                while i < (_len - 1) and nums[i + 1] == target:
                    i += 1
                while j > 0 and nums[j - 1] == target:
                    j -= 1
                start = j; end = i
                return [start, end]
            elif mid_val < target:
                L += (len(nums[L:R])) // 2
                mid_i = L + ((len(nums[L:R])) // 2)
                mid_val = nums[mid_i]
            else:
                R = mid_i
                mid_i = len(nums[L:R+1]) // 2
                mid_val = nums[mid_i]
        if len(nums[L:R+1]) == 2:
            win = nums[L:R+1]
            if win[0] == target and win[1] == target:
                start, end = L, R
            elif win[0] == target and win[1] != target:
                start = end = L
            elif win[0] != target and win[1] == target:
                start = end = R

        return [start, end]


def main():
    print(Solution().searchRange([], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([1,2,3,4,5,6], 2))
    print(Solution().searchRange([1, 1, 1, 1, 5, 6], 1))
    print(Solution().searchRange([1, 1, 1, 1, 1, 1], 1))
    print(Solution().searchRange([1], 4))
    print(Solution().searchRange([1, 4], 4))
    print(Solution().searchRange([1, 2, 3], 3))
    print(Solution().searchRange([1, 2, 3, 4, 5, 6, 7, 8], 8))
    print(Solution().searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
    print(Solution().searchRange([1], 0))
    print(Solution().searchRange([2,2], 1))
    print(Solution().searchRange([0, 1, 2, 3, 4, 4, 4], 2))
    print(Solution().searchRange([0, 0, 1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10], 4))
    print(Solution().searchRange([2, 2], 2))
    print(Solution().searchRange([1, 3], 1))


if __name__ == '__main__':
    main()


# expected
# [-1,-1]
# [3,4]
# [1,1]
# [0,3]
# [0,5]
# [-1,-1]
# [1,1]
# [2,2]
# [7,7]
# [2,5]
# [-1,-1]
# [-1,-1]
# [2,2]
# [7,8]
# [0, 1]
# [0, 0]

# LC input
# []
# 8
# [5,7,7,8,8,10]
# 8
# [1,2,3,4,5,6]
# 2
# [1, 1, 1, 1, 5, 6]
# 1
# [1, 1, 1, 1, 1, 1]
# 1
# [1]
# 4
# [1,4]
# 4
# [1,2,3]
# 3
# [1,2,3,4,5,6,7,8]
# 8
# [1,2,3,3,3,3,4,5,9]
# 3
# [1]
# 0
# [2,2]
# 1
# [0,1,2,3,4,4,4]
# 2
# [0,0,1,1,1,2,3,4,4,5,6,7,7,7,8,8,8,8,9,9,10]
# 4
# [2,2]
# 2
# [1,3]
# 1

# Instructions
"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""