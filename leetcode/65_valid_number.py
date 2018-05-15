# Instructions
"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

import string
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _len = len(s)
        alpha = ['abcdfghijklmnopqrstuvwxyz']
        nums = list('12345678990')
        if _len == 1:
            return s.isnumeric()
        if all([x not in s for x in nums]):
            return False

        if s.startswith('e'):
            return False
        i = 0
        while i < len(s):
            while i < _len and s[i] not in nums:
                i += 1
            if i >= _len:
                break
            if s[i] in alpha:
                return False
            if s[i] == ' ':
                if (s[i:] != (' ' * (_len - i))):
                    return False
            i += 1

        return True





def main():
    print(Solution().isNumber("0"))      # True
    print(Solution().isNumber("0.1"))    # True
    print(Solution().isNumber("abc"))    # False
    print(Solution().isNumber("1 a"))    # False
    print(Solution().isNumber("2e10"))   # True
    print(Solution().isNumber("."))      # False
    print(Solution().isNumber("1 "))     # True
    print(Solution().isNumber(" "))      # False
    print(Solution().isNumber(" 0"))     # True


if __name__ == '__main__':
    main()