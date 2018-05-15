"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        retlst = []
        for i in range(0, num+1):
            _this = 0
            while i > 0:
                if i & 1:
                    _this += 1
                i >>= 1
            retlst.append(_this)
        return retlst

def main():
    print(Solution().countBits(2))  # [0, 1, 1]
    print(Solution().countBits(5))  # [0, 1, 1, 2, 1, 2]


# LC input
# 2
# 5

if __name__ == '__main__':
    main()