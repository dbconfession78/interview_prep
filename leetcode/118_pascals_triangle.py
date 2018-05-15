"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

import sys
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        retlst = [[1],[1,1]]
        if numRows == 2:
            return retlst
        for i in range(3, numRows+1):
            stk = [x for x in retlst[-1]]
            _this = []
            while stk:
                x = stk.pop()
                if stk:
                    _this.append(stk[-1] + x)
            retlst.append([retlst[-1][0]] + _this + [retlst[-1][-1]])
        return retlst



def print_retlst(lst):
    for row in lst:
        sys.stdout.write('[')
        for i, n in enumerate(row):
            sys.stdout.write(str(n))
            if i < len(row)-1:
                sys.stdout.write(', ')
            else:
                print(']')
    print()


def main():
    # [
    #      [1],
    #     [1,1],
    #    [1,2,1],
    #   [1,3,3,1],
    #  [1,4,6,4,1]
    # ]
    # print_retlst(Solution().generate(0))
    print_retlst(Solution().generate(1))
    print_retlst(Solution().generate(2))
    print_retlst(Solution().generate(3))
    print_retlst(Solution().generate(4))
    print_retlst(Solution().generate(5))
    print_retlst(Solution().generate(6))
    print_retlst(Solution().generate(7))
    print_retlst(Solution().generate(8))


if __name__ == '__main__':
    main()