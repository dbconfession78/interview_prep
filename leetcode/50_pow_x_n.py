"""
Implement pow(x, n).
http://www.cplusplus.com/reference/valarray/pow/

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
"""
class Solution(object):
    # def myPow_PRACTICE(self, x, n):
    def myPow(self, x, n):
        return

    def myPow_PASSED(self, x, n):
    # def myPow(self, x, n):
        if n == 0:
            return 1.0
        MAX = 2**31-1
        if n > MAX-1:
            if x < 1 and x > 0:
                return 0.0
            if x < 0:
                return x
            return 1.0
        if n < -MAX:
            if x < 1 and x > 0:
                return 0.0
            if x > 1:
                return 0.0
            return 1.0


        is_neg = False
        retval = x
        if n < 0:
            is_neg = True
            n *= -1
        while n > 1:
            retval *= x
            n -= 1
        if is_neg:
            retval  = 1 / retval
        return retval


def main():
    print(Solution().myPow(2.0, 10))                 # 1024
    print(Solution().myPow(2.1, 3))                  # 9.261
    print(Solution().myPow(34.00515, -3))           # 3e-05 (or 2.543114507074558e-05)
    print(Solution().myPow(0.44528, 0))             # 1.0
    print(Solution().myPow(0.00001, 2147483647))    # 0.0
    print(Solution().myPow(1.00000, 2147483647))    # 1.0
    print(Solution().myPow(1.00000, -2147483648))   # 1.0
    print(Solution().myPow(2.00000, -2147483648))   # 0.0
    print(Solution().myPow(-1.00000, 2147483647))   # -1.0


# LC input
# 2.0
# 10
# 2.1
# 3
# 34.00515
# -3
# 0.44528
# 0
# 0.00001
# 2147483647
# 1.00000
# 2147483647
# 1.00000
# -2147483648
# 2.00000
# -2147483648
# -1.00000
# 2147483647
if __name__ == '__main__':
    main()


"""
class Solution:
    def func(self):
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
