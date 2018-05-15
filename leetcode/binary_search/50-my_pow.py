class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

def main():
    print(Solution().myPow(2.00000, 10))


if __name__ == '__main__':
    main()

# Instructions
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