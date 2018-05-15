"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    # def reverseStr_PRACTICE(self, s, k):
    def reverseStr(self, s, k):
        return

    def reverseStr_PASSED(self, s, k):
    # def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # reverse the first k characters for every 2k characters
        _len = len(s)
        if _len == 1:
            return s
        s = list(s)
        i = 0
        rng = k * 2
        while i < len(s):
            rem = len(s) - i
            if rem < k:
                for j in range(rem):
                    s.insert(i+j, s.pop(-1))
            elif rem < rng and rem >= k:
                for j in range(k):
                    s.insert(i+j, s.pop(i+(k-1)))
            else:
                for j in range(k):
                    s.insert(i+j, s.pop(i+(k-1)))
            i += rng
        return ''.join(s)



def main():
    print(Solution().reverseStr("abcdefg", 2))     # "bacdfeg"
    print(Solution().reverseStr("abcdef", 2))      # "bacdfe"
    print(Solution().reverseStr("abcd", 4))        # "dcba"
    print(Solution().reverseStr("a", 2))           # "a"
    print(Solution().reverseStr("abcdefg", 8))         # "abcdefg"

# LC input
# "abcdefg"
# 2
# "abcdef"
# 2
# "abcd"
# 4
# "a"
# 2
# "abcdefg"
# 8

if __name__ == '__main__':
    main()