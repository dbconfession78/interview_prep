# Instructions
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    # 11.5 min
    # def isPalindrome_PRACTICE(self, x):
    def isPalindrome(self, x):
        return


    # def isPalindrome_PASSED(self, x):
    def isPalindrome(self, x):
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
    print(Solution().isPalindrome(-2147483648))     # False
    print(Solution().isPalindrome(23432))           # True
    print(Solution().isPalindrome(234432))           # True
    print(Solution().isPalindrome(1000021))           # False


# LC input
# -2147483648
# 23432
# 234432

if __name__ == '__main__':
    main()