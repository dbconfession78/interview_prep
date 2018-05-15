import sys
class Solution:
    # def divide_MINE(self, dividend, divisor):
    def divide(self, dividend, divisor):
        """
         :type dividend: int
         :type divisor: int
         :rtype: int
         """
        neg = False
        if (dividend < 0) != (divisor < 0):
            neg = True

        _max = ((2 ** 32) // 2) - 1
        _min = -_max - 1
        step = divisor = abs(divisor)
        rem = abs(dividend)
        mult = 1
        retval = 0

        while rem >= divisor:
            if step > rem:
                step = divisor
                mult = 1
            rem -= step
            retval += mult
            mult += mult
            step += step

        if neg:
            return max(_min, -retval)
        return min(_max, retval)

    def divide_LC_bit_shift(self, dividend, divisor):
    # def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend

        if divisor < 0:
            sign = -sign
            divisor = -divisor

        if dividend < divisor:
            return 0

        quotient = self.divideHlp(dividend, divisor)

        return max(-2**31, min(sign * quotient, 2**31-1))

    def divideHlp(self, dividend, divisor):
        higher_divisor = divisor
        step = 0
        while higher_divisor < 2**31-1:
            higher_divisor <<= 1
            step += 1
        print()

        quotient = 0
        while higher_divisor >= divisor:
            remainder = dividend - higher_divisor
            if remainder >= 0:
                dividend = remainder
                quotient += 2 ** step
            higher_divisor >>= 1
            step -= 1
        return quotient


def main():
    """Test cases"""
    print(Solution().divide(0, 1))
    print(Solution().divide(10, 3))
    print(Solution().divide(-1, 1))
    print(Solution().divide(1, 2))
    print(Solution().divide(-2147483648, -1))
    print(Solution().divide(2147483647, 1))
    print(Solution().divide(-2147483648, 1))
    print(Solution().divide(2147483647, 2))

# expected output
# 0
# 3
# -1
# 0
# 2147483647
# 2147483647
# -2147483648
# 1073741823

# LC input
# 0
# 1
# 10
# 3
# -1
# 1
# 1
# 2
# -2147483648
# -1
# 2147483647
# 1
# -2147483648
# 1
# 2147483647
# 2

def divide_sol(self, dividend, divisor):
    neg=((dividend < 0) != (divisor < 0))
    dividend = rem = abs(dividend)
    divisor  = div  = abs(divisor)
    Q = 1
    ans = 0
    while rem >= divisor:
        rem -= div
        ans  += Q
        Q    += Q
        div  += div
        if rem < div:
            div = divisor
            Q = 1
    if neg:
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483647)

if __name__ == '__main__':
    main()
# Instructions:
"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""