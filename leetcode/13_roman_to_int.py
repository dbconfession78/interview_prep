#!/usr/bin/python3
from sys import argv
from os import path


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        retval = 0
        nxt = None
        for (i, char) in enumerate(s):
            num = nxt if nxt else dct.get(char)
            if i == len(s) - 1:
                return retval + num
            nxt = dct.get(s[i+1])
            retval = (retval - num) if num < nxt else (retval + num)
        return retval


def main():
    # if len(argv) < 2:
    #     print('USAGE: ./{} <roman numeral>'.format(path.basename(__file__)))
    #     return
    # print(Solution().romanToInt(argv[1]))

    """Test cases"""
    print(Solution().romanToInt("DCXXI"))  # 621
    print(Solution().romanToInt("D"))  # 500
    print(Solution().romanToInt("IXVC"))  # 104
    print(Solution().romanToInt("IVXLCDM"))  # 334



# LC input
# "DCXXI"
# "D"
# "IXVC"

if __name__ == '__main__':
    main()
