# Instructions
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1
"""

class Solution:
    # def isHappy_PRACTICE(self, n):
    def isHappy(self, n):
        return





    def isHappy_PASSED(self, n):
    # def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # replace number with the sum of the square of its digits
        # repeat until number is 1
        lst = []
        while n != 1:
            n = self.sum_squares2(n)
            if n in lst:
                return False
            else:
                lst.append(n)
        return True

    def sum_squares2(self, n):
        retval = 0
        while n > 0:
            retval += (n % 10)**2
            n //= 10
        return retval


def main():
    print(Solution().isHappy(0))        # False
    print(Solution().isHappy(1))        # True
    print(Solution().isHappy(2))        # False
    print(Solution().isHappy(3))        # False
    print(Solution().isHappy(4))        # False
    print(Solution().isHappy(5))        # False
    print(Solution().isHappy(6))        # False
    print(Solution().isHappy(7))        # True
    print(Solution().isHappy(8))        # False
    print(Solution().isHappy(9))        # False
    print(Solution().isHappy(10))       # True
    print(Solution().isHappy(11))       # False
    print(Solution().isHappy(12))       # False
    print(Solution().isHappy(13))       # True
    print(Solution().isHappy(14))       # False
    print(Solution().isHappy(15))       # False
    print(Solution().isHappy(16))       # False
    print(Solution().isHappy(17))       # False
    print(Solution().isHappy(18))       # False
    print(Solution().isHappy(19))       # True
    print(Solution().isHappy(20))       # False
    print(Solution().isHappy(21))       # False
    print(Solution().isHappy(23))       # True
    print(Solution().isHappy(24))       # False
    print(Solution().isHappy(25))       # False
    print(Solution().isHappy(37))       # False
    print(Solution().isHappy(1000))     # True
    print(Solution().isHappy(10000))    # True
    print(Solution().isHappy(100000))   # True
    print(Solution().isHappy(100001))   # False

# expected

# false
# true
# false
# false
# false
# false
# false
# true
# false
# false
# true
# false
# false
# true
# false
# false
# false
# false
# false
# true
# false
# false
# true
# false
# false
# false
# true
# true
# true
# false

# LC input
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 23
# 24
# 25
# 37
# 1000
# 10000
# 100000
# 1000


if __name__ == '__main__':
    main()