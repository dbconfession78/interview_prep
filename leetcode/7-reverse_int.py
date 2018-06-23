"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
from sgk_test import test

class Solution(object):
    # def reverse_PRACTICE(self, x):
    def reverse(self, x):
        return 0


    def reverse_PASSED(self, x):
    # def reverse(self, x):
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


test(321, Solution().reverse(123))
test(-321, Solution().reverse(-123))
test(21, Solution().reverse(120))
test(0, Solution().reverse(-1534236469))
test(0, Solution().reverse(1534236469))
test(0, Solution().reverse(0))
