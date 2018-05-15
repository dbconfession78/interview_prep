# Instructions
"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {'A':1, 'B':2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G':7,
               'H': 8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
               'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21,
               'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

        m = 0
        lst = list(s)
        retval = 0
        while lst:
            x = lst.pop()
            retval += (26**m) * dct.get(x)
            m += 1
        return retval


def main():
    print(Solution().titleToNumber('AA'))   # 27
    print(Solution().titleToNumber('BA'))   # 53
    print(Solution().titleToNumber('CBA'))  # 2081

# LC input
# "AA"
# "BA"
# "CBA"


if __name__ == '__main__':
    main()
