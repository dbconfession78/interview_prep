# Instructions
"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from itertools import permutations


class Solution:
    def permute_LC(self, nums):
    # def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
            perms = new_perms
        return perms

    # def permute_MINE(self, nums):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(perm) for perm in permutations(nums, len(nums))]


def main():
    print(Solution().permute([1, 2, 3]))
    # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

    print(Solution().permute([5, 9, 3, 7]))
    # [[5, 9, 3, 7], [5, 9, 7, 3], [5, 3, 9, 7], [5, 3, 7, 9], [5, 7, 9, 3], [5, 7, 3, 9], [9, 5, 3, 7], [9, 5, 7, 3], [9, 3, 5, 7], [9, 3, 7, 5], [9, 7, 5, 3], [9, 7, 3, 5], [3, 5, 9, 7], [3, 5, 7, 9], [3, 9, 5, 7], [3, 9, 7, 5], [3, 7, 5, 9], [3, 7, 9, 5], [7, 5, 9, 3], [7, 5, 3, 9], [7, 9, 5, 3], [7, 9, 3, 5], [7, 3, 5, 9], [7, 3, 9, 5]


if __name__ == '__main__':
    main()


# plan -> keys:
# keys -> debug (first submit):
# debug -> accepted:
# Total