# Instructions
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter
class Solution:
    # def firstUniqChar_LC(self, s):
    def firstUniqChar(self, s):
        dct = Counter(s)
        for i, c in enumerate(s):
            if dct.get(c) == 1:
                return i
        return -1

    def firstUniqChar_MINE(self, s):
    # def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        dct = {}
        lst = []
        while i < len(s):
            c = s[i]
            if dct.get(c):
                if c in lst:
                    lst.pop(lst.index(c))
            else:
                lst.append(c)
                if i == 0:
                    dct[c] = 'X'
                else:
                    dct[c] = i
            i += 1
        if not lst:
            return -1
        retval = dct.get(lst[0])
        return 0 if retval == 'X' else retval




def main():
    print(Solution().firstUniqChar("leetcode"))                         # 0
    print(Solution().firstUniqChar("loveleetcode"))                     # 2
    print(Solution().firstUniqChar("lardeatcode"))                      # 0
    print(Solution().firstUniqChar("abcdefgghijklmmnopqrstuvvwxyz"))    # 0
    print(Solution().firstUniqChar("loveleetcvode"))                    # 7
    print(Solution().firstUniqChar(""))                                 # 0


# LC input
# "leetcode"
# "loveleetcode"
# "lardeatcode"
# "abcdefgghijklmmnopqrstuvvwxyz"
# "loveleetcvode"
# ""


if __name__ == '__main__':
    main()