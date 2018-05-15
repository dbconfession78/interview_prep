class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        if len(nums) == 0:
            return 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                i += 1
            else:
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    nums.pop(i)
        return i + 1


def main():
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6]))
    print(Solution().removeDuplicates([]))
    print(Solution().removeDuplicates([1, 1]))


if __name__ == '__main__':
    main()

# expected
# 2
# 6
# 0
# 1

# LC input
# [1,1]
# [1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6]
# []
# [1,1]


# Instructions
"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""