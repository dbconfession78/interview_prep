class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i_s = i_p = 0
        match_count = 0
        running = False

        if s == p:
            return True

        while i_p < len(p) and i_s < len(p) and i_s < len(s):
            if s[i_s] != p[i_p]:

                # handle STAR
                if p[i_p] == '*':
                    i = i_p - 1
                    while i > 0 and p[i] == '.':
                        i -= 1
                    c = p[i]
                    if c == '.':
                        i_s = len(s)
                    while i_s < len(s) and s[i_s] == c:
                        i_s += 1
                    i_p += 1
                    if i_s == len(s) and i_p != len(p):
                        return False

                # handle DOT
                elif p[i_p] == '.':
                    i_s += 1
                    i_p += 1
                else:
                    return False
            else:
                i_s += 1
                i_p += 1

        return True


def main():
    # print(Solution().isMatch('aa', 'a'))        # F
    # print(Solution().isMatch('aa', 'aa'))       # T
    # print(Solution().isMatch('aaa', 'aa'))      # F
    # print(Solution().isMatch('aa', 'a*'))       # T
    # print(Solution().isMatch('aa', '.*'))       # T
    # print(Solution().isMatch('ab', '.*'))       # T
    # print(Solution().isMatch('aab', 'c*a*b'))   # T
    # print(Solution().isMatch('aab', '...'))     # T
    # print(Solution().isMatch('aab', '..'))      # F
    # print(Solution().isMatch('abcd', 'd*'))     # F
    # print(Solution().isMatch('ab', '.*c'))      # F
    # print(Solution().isMatch('aaa', 'aaaa'))    # F
    print(Solution().isMatch('aaa', 'a*a'))     # T
    print(Solution().isMatch('aaa', 'a*aa'))    # T
    print(Solution().isMatch('aaa', 'a*aaa'))   # F
    print(Solution().isMatch('aaa', 'a*b'))     # F


# LC input
# "aa"
# "a"
# "aa"
# "aa"
# "aaa"
# "aa"
# "aa"
# "a*"
# "aa"
# ".*"
# "ab"
# ".*"
# "aab"
# "c*a*b"
# "aab"
# "..."
# "aab"
# ".."
# "abcd"
# "d*"
# "ab"
# ".*c"
# "aaa"
# "aaaa"
# "aaa"
# "a*a"
# "aaa"
# "a*aa"
# "aaa"
# "a*aaa"
# "aaa"
# "a*b"

if __name__ == '__main__':
    main()

# Instructions
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""