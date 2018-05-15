# Instructions
"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        nums.sort()
        n = _len // 2
        pairs = []
        i = 0
        while i < _len - 1:
            pairs.append([nums[i]
nums[i + 1]])
            i += 2

        _sum = 0
        for pair in pairs:
            _sum += min(pair)
        return _sum

# plan -> keys: 8 min
# keys -> debug (first submit): 5 min
# debug -> accepted: 0
# Total 13 min
def main():
    print(Solution().arrayPairSum([1, 4, 3, 2]))    # 4


# LC input
# [1,4,3,2]
if __name__ == '__main__':
    main()

"""
--


def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""