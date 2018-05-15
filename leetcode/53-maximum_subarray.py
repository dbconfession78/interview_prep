# Instructions
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def max_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -(2**31)
        _len = len(nums)
        if not nums:
            return max_sum
        for i in range(_len):
            for j in range(_len):
                if i == j:
                    _sum = nums[i]
                else:
                    _sum = sum(nums[i:j+2])
                if _sum > max_sum:
                    max_sum = _sum
        return max_sum


def main():
    # print(Solution().max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    # print(Solution().max_subarray([-1]))                             # -1
    # print(Solution().max_subarray([]))                      # -2147483648
    # print(Solution().max_subarray([-2, -1]))                         # -1
    print(Solution().max_subarray([-2,-3,-1]))                      # -1



#LC input
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# [-1]
# []
# [-2,-1]
# [-2,-3,-1]




if __name__ == '__main__':
    main()

# LC input
