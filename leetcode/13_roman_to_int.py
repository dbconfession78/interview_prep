#!/usr/bin/python3
from sys import argv
from os import path


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
        skip_next = False

        retval = 0
        for (i, char) in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            this = dict[char]
            if i < len(s)-1:
                next = dict[s[i+1]]
                if (next > this):
                    retval += (next-this)
                    skip_next = True
                    continue
            retval += dict[char]
        return retval


def main():
    if len(argv) < 2:
        print('USAGE: ./{} <roman numeral>'.format(path.basename(__file__)))
        return
    print(Solution().romanToInt(argv[1]))


if __name__ == '__main__':
    main()
