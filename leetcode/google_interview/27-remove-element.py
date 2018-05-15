# Instructions
"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3]
val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution:
    # def removeElement_NO_POP(self, nums, val):
    def removeElement(self, nums, val):
        i = 0
        tmp = [x for x in nums]
        while i < len(tmp):
            if tmp[i] == val:
                tmp = tmp[:i] + tmp[i+1:]
            i += 1

        for i in range(len(tmp)):
            nums[i] = tmp[i]
        print(nums)
        return i

    def removeElement_POP(self, nums, val):
    # def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        if nums == []:
            return 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)


def main():
    nums = [3, 2, 2, 3]
    print(nums[:Solution().removeElement(nums, 3) + 1])

# expected
# return: 2, output [2, 2]
# *if printed right before return, nums should be [2,2,2,3]


# LC input
# [3,2,2,3]
# 3


if __name__ == '__main__':
    main()