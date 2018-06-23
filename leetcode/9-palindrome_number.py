# Instructions
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
from sgk_test import test
class Solution(object):
    # def isPalindrome_PRACTICE(self, x):
    def isPalindrome(self, x):
        return



    def isPalindrome_PASSED(self, x):
    # def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        m = 10**(len(str(x)) - 1)

        while m > 1:
            left = x // m
            right = x % 10
            if left != right:
                return False
            x %= m
            x //= 10
            m //= 100
        return True


def main():
    test(False, Solution().isPalindrome(-6))
    test(True, Solution().isPalindrome(6))
    test(False, Solution().isPalindrome(-2147483648))
    test(True, Solution().isPalindrome(23432))
    test(True, Solution().isPalindrome(234432))
    test(False, Solution().isPalindrome(1000021))


# LC input
# -2147483648
# 23432
# 234432

if __name__ == '__main__':
    main()