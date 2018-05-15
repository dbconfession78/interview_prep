"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        retval = float('inf')
        l, r = 0, len(nums)-1
        while l < r:

            m = (l + r) // 2
            v = nums[m]

            if v < nums[m+1]:
                if v < nums[r]:
                    r = m
                elif v > nums[r]:
                    l = m + 1
            elif v > nums[m+1]:
                l = m + 1

        if nums[m] < nums[m+1]:
            return nums[m]
        else:
            return nums[m+1]



def main():
    print(Solution().findMin([1]))                       # 1
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))    # 0
    print(Solution().findMin([4, 5, 6, 7, 8, 1, 2]))    # 1

# LC Input
# [1]
# [4, 5, 6, 7, 0, 1, 2]
# [4, 5, 6, 7, 8, 1, 2]


if __name__ == '__main__':
    main()