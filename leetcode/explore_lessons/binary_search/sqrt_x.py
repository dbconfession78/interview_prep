"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

"""


class Solution:
    def mySqrt_2(self, x):
    # def mySqrt(self, x):
        return

    # def mySqr1(self, x):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while True:
            m = l + (r-l) // 2
            if m*m == x:
                return m
            elif m*m > x:
                r = m
            elif m*m < x:
                n = (l+1) + (r - (l+1)) // 2
                if n*n > x:
                    m += 1
                while m*m <= x:
                    m += 1
                return m-1



def main():
    print(Solution().mySqrt(4))     #2
    print(Solution().mySqrt(8))     #2
    print(Solution().mySqrt(81))    #9
    print(Solution().mySqrt(12))    #3
    print(Solution().mySqrt(100))  # 10
    print(Solution().mySqrt(0))     # 0
    print(Solution().mySqrt(1))     # 1
    print(Solution().mySqrt(2))     # 1
    print(Solution().mySqrt(3))     # 1
    print(Solution().mySqrt(5))     # 2

# LC Input 4
# 4
# 8
# 81
# 12
# 100
# 0
# 1
# 2
# 3
# 5

if __name__ == '__main__':
    main()