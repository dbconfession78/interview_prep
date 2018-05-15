#!/usr/bin/python3
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        factor = 1
        retval = 0
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1

        while int(x % 10) == 0:
            x /= 10
        num = x

        while num > 9:
            num = int(num / 10)
            factor *= 10

        num = int(x)
        while num > 9:
            retval = int(retval) + (int(num % 10) * factor)
            factor = int(factor / 10)
            num = int(num / 10)
        retval += num

        if is_neg:
            retval *= -1
        if retval > 2147483647 or retval < -2147483648:
            return 0

        return retval


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(-1534236469))
print(Solution().reverse(1534236469))

#LC input
# 123
# -123
# 120
# -1534236469
# 1534236469
