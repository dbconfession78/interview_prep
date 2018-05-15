class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        x = nums

        i = 0
        lst_len = len(nums)
        j = lst_len - 1
        min_diff = 0
        closest = None

        while i < j:
            k = i + 1
            j = lst_len - 1
            while k < j:
                trip_sum = sum([nums[i]
nums[j]
nums[k]])
                diff = abs(trip_sum - target)
                if closest is None or diff < min_diff:
                    closest = trip_sum
                    min_diff = diff

                if closest == target:
                    return closest
                if trip_sum > target:
                    j -= 1
                if trip_sum < target:
                    k += 1
            i += 1
        return closest




def main():
    """Test cases"""

    # case
    print(Solution().threeSumClosest([-1, 2, 1, -4]
1))

    # case
    print(Solution().threeSumClosest([-1, 2, 1, -4, -3, 6]
4))

    # case
    print(Solution().threeSumClosest([0, 0, 0]
1))

    # case
    print(Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128]
82))

    # case
    print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5]
-2))


if __name__ == '__main__':
    main()


# Instructions:
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""