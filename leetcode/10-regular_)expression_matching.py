"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

from sgk_test import test
from collections import defaultdict
class Solution:
    # def isMatch_PRACTICE(self, s, p):
    def isMatch(self, s, p):
        return

    def isMatch_SOL(self, s, p):
    # def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

def main():
    test(False, Solution().isMatch('aa', 'a'))
    test(True, Solution().isMatch('aa', 'aa'))
    test(False, Solution().isMatch('aaa', 'aa'))
    test(True, Solution().isMatch('aa', 'a*'))
    test(True, Solution().isMatch('aa', '.*'))
    test(True, Solution().isMatch('ab', '.*'))
    test(True, Solution().isMatch('aab', 'c*a*b'))
    test(True, Solution().isMatch('aab', '...'))
    test(False, Solution().isMatch('aab', '..'))
    test(False, Solution().isMatch('abcd', 'd*'))
    test(False, Solution().isMatch('ab', '.*c'))
    test(False, Solution().isMatch('aaa', 'aaaa'))
    test(True, Solution().isMatch('aaa', 'a*a'))
    test(True, Solution().isMatch('aaa', 'a*aa'))
    test(True, Solution().isMatch('aaa', 'a*aaa'))
    test(False, Solution().isMatch('aaa', 'a*b'))
    test(False, Solution().isMatch('a', '.*..a*'))
    test(False, Solution().isMatch('', 'b.'))
    test(False, Solution().isMatch('a', 'b*.c'))
    test(False, Solution().isMatch('a', 'ab*a'))
    test(True, Solution().isMatch("ab", ".*.."))
    test(True, Solution().isMatch("ab", ".*..c*"))


if __name__ == '__main__':
    main()
