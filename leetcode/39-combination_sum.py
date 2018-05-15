# Instructions
"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution:
    # 16 min
    # def combinationSum_PRACTICE(self, candidates, target):
    def combinationSum(self, candidates, target):
        return




    def combinationSum_STK(self, candidates, target):
    # def combinationSum(self, candidates, target):
        candidates.sort()
        retlst = []
        stk = [(target, [])]

        while stk:
            remain, combo = stk.pop()
            if remain == 0:
                retlst.append(combo)
                continue
            for elem in candidates:
                if elem > remain:
                    break
                if combo and elem < combo[-1]:
                    continue
                stk += [(remain - elem, combo + [elem])]


        return retlst



    def combinationSum_REC(self, candidates, target):
    # def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retlst = []
        candidates.sort()

        def helper(remain, stk):
            if remain == 0:
                retlst.append(stk)
                return

            for elem in candidates:
                if elem > remain:
                    break
                if stk and elem < stk[-1]:
                    continue
                helper(remain - elem, stk + [elem])

        helper(target, [])
        return retlst


def main():
    # print(Solution().combinationSum([2, 3, 6, 7], 7))   # [[2, 2, 3], [7]]
    # print(Solution().combinationSum([2, 3, 5], 7))      # [[2, 2, 3], [2, 5]]
    print(Solution().combinationSum([8, 7, 4, 3], 11))  # [[3, 4, 4], [3, 8], [4, 7]]
    # print(Solution().combinationSum([], 1))             # []
    # print(Solution().combinationSum([1], 2))            # [[1, 1]]
    # print(Solution().combinationSum([1], 3))            # [[1, 1, 1]]
    # print(Solution().combinationSum([1, 2], 3))         # [[1, 1, 1], [1, 2]]


# LC input
# [2,3,6,7]
# 7
# [2, 3, 5]
# 7
# [8,7,4,3]
# 11
# []
# 1
# [1]
# 2
# [1]
# 3
# [1,2]
# 3

if __name__ == '__main__':
    main()


# plan -> keys:
# keys -> debug (first submit):
# debug -> accepted:
# Total
