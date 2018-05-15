# Instructions
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        n = len(nums)
        majority = n // 2
        counter = Counter()
        i = 0
        if n == 1:
            return nums[0]
        while i < n:
            counter[nums[i]] += 1
            if counter[nums[i]] > majority:
                return nums[i]
            i += 1


# plan -> keys: 7 min
# keys -> debug (first submit): + 3 min
# debug -> accepted: + 6 mins
# Total 16
def main():
    print(Solution().majorityElement([1]))
    print(Solution().majorityElement([1, 5, 6, 1, 6, 5, 1, 1, 1, 6, 1, 6, 1, 5, 1, 1, 1, 6, 6, 6, 1, 1, 1, 1]))
    print(Solution().majorityElement([2,2]))

# LC input
# [1]
# [1, 5, 6, 1, 6, 5, 1, 1, 1, 6, 1, 6, 1, 5, 1, 1, 1, 6, 6, 6, 1, 1, 1, 1]
# [2, 2]

if __name__ == '__main__':
    main()

"""
--


def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""