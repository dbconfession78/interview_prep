# Instructions
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

import string
class Solution:
    # def isPalindrome_PRACTICE(self, s):
    def isPalindrome(self, s):
        return


    def isPalindrome_PYTHONIC_PASSED(self, s):
    # def isPalindrome(self, s):
        s = ''.join([x for x in s if x != ' ' and x not in string.punctuation]).lower()
        return True if s == s[::-1] else False

    def isPalindrome_PASSED(self, s):
    # def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x.lower() for x in s if x.isalnum()]
        _len = len(s)
        if s == s[::-1]:
            return True
        i = 0
        j = _len - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


def main():
    print(Solution().isPalindrome(""))      # True
    print(Solution().isPalindrome("a."))    # True
    print(Solution().isPalindrome("0P"))    # False
    print(Solution().isPalindrome("laal"))  # True
    print(Solution().isPalindrome("aba"))   # True
    print(Solution().isPalindrome("A man, a plan, a canal: Panama")) # True
    print(Solution().isPalindrome("ab"))    # False
    print(Solution().isPalindrome("abc"))   # False
    print(Solution().isPalindrome("aaaaaaaaaaaaaaaaa")) # True
    print(Solution().isPalindrome("a"))                 # True

# expected
# true
# true
# false
# true
# true
# true
# false
# false
# true
# true



# LC input
# ""
# "0P"
# "a."
# "laal"
# "aba"
# "A man, a plan, a canal: Panama"
# "ab"
# "abc"
# "aaaaaaaaaaaaaaaaa"
# "a"
if __name__ == '__main__':
    main()