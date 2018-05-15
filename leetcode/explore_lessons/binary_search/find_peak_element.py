"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0

        left, right = 0, len(nums)
        while left < right:
            if left == right:
                break
            m = (left + right) // 2

            if m < len(nums) - 1 and nums[m] > nums[m + 1]:
                if nums[m] >= nums[m-1]:
                    return m

            if m < len(nums)-1 and nums[m + 1] > nums[m] > nums[m - 1]:
                left = m + 1
            else:
                right = m

        if left > 0:
            if nums[left] > nums[left-1]:
                return left
            else:
                return left - 1
        elif nums[left] > nums[left+1]:
            return left
        else:
            return left+1


def main():
    print(Solution().findPeakElement([1, 2, 3, 1]))                # 2
    print(Solution().findPeakElement([3, 2, 1, 1]))                # 0
    print(Solution().findPeakElement([2, 3, 4, 4, 4, 3, 2, 1]))    # 2 or 4
    print(Solution().findPeakElement([1]))                         # 0
    print(Solution().findPeakElement([1, 2]))                      # 1
    print(Solution().findPeakElement([3, 2, 1]))                   # 0
    print(Solution().findPeakElement([1, 2, 3]))                   # 2

# LC Input
# [1,2,3,1]
# [3,2,1,1]
# [2,3,4,4,4,3,2,1]
# [1]
# [1,2]
# [3,2,1]
# [1,2,3]


if __name__ == '__main__':
    main()
