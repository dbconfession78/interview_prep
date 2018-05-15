# Instructions
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    # def combine_LC(self, n, k):
    def combine(self, n, k):
        stk = []
        retlst = []
        x = 1
        while True:
            _len = len(stk)
            if _len == k:
                retlst.append(stk[:])
            if _len == k or x > n - k + _len + 1:
                if not stk:
                    return retlst
                x = stk.pop() + 1
            else:
                stk.append(x)
                x += 1



    def combine_MINE(self, n, k):
    # def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        retlst = []
        stk = [x for x in range(1, n+1)]

        for i in range(n):
            for j in range(n-i):
                lst = [stk[-1]] + stk[0+(n-k-i):k+1-i][::-1]
                print(lst)
                retlst.append(lst)
                stk.insert(0,stk.pop())
            i += 1
        print()



        print(len(retlst))
        return retlst


def main():
    print(Solution().combine(4, 2))
    # [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]

    # print(Solution().combine(6, 4))


if __name__ == '__main__':
    main()


# plan -> keys:
# keys -> debug (first submit):
# debug -> accepted:
# Total
"""
--


def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""