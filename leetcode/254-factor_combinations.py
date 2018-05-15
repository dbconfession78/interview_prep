# Instructions
"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples:
input: 1
output:
[]
input: 37
output:
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""


class Solution:
    # def getFactors_PRACTICE(self, n):
    def getFactors(self, n):
        #TODO your code goes here
        return

    # def getFactors_REC(self, n):
    def getFactors(self, n):
        def helper(n, i, combo, combos):
            while i * i <= n:
                if n % i == 0:
                    combos += [combo + [n // i, i]]
                    helper(n // i, i, combo + [i], combos)
                i += 1
            return combos
        return helper(n, 2, combo=[], combos=[])

    def getFactors_STK(self, n):
    # def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        todo, combos = [(n, 2, [])], []
        while todo:
            n, i, combo = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    # nxt 2 lns r same. ln1: ',' is ln2: []
                    combos += combo + [i, n // i],    # ln1
                    # combos += [combo + [i, n // i]] # ln2
                    todo += (n // i, i, combo + [i]),
                i += 1
        return combos


def main():
    # [2, 6]
    # [3, 4]
    # [2, 2, 3]
    n = 12
    print()
    print(f'{n}\'s factor combos')
    ret = Solution().getFactors(n)
    for x in ret:
        print(x)

    #[2, 16]
    # [4, 8]
    # [2, 2, 8]
    # [2, 4, 4]
    # [2, 2, 2, 4]
    # [2, 2, 2, 2, 2]
    n = 32
    print()
    print(f'{n}\'s factor combos')
    ret = Solution().getFactors(n)
    for x in ret:
        print(x)

    # [3, 27]
    # [9, 9]
    # [3, 3, 9]
    # [3, 3, 3, 3]
    n = 81
    print()
    print(f'{n}\'s factor combos')
    ret = Solution().getFactors(81)
    for x in ret:
        print(x)

    # [3, 9]
    # [3, 3, 3]
    print()
    print(f'{n}\'s factor combos')
    ret = Solution().getFactors(27)
    for x in ret:
        print(x)


if __name__ == '__main__':
    main()