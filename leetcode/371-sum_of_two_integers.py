class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # '^' gets different bits and '&' gets double 1s, '<<' moves carry
            # setting a and b on one line allows b to use a's original value
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)


def main():
    print(Solution().getSum(1, 2))
    print(Solution().getSum(4, 4))
    print(Solution().getSum(5, 4))
    print(Solution().getSum(-2, 4))
    print(Solution().getSum(2, -4))
    print(Solution().getSum(100, -900))
    print(Solution().getSum(-12, -8))


#LC input
# 1
# 2
# 4
# 4
# -2
# 4
# 2
# -4
# 100
# -900
# -12
# -8


if __name__ == '__main__':
    main()


# Instructions
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

"""