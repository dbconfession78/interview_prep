# Instructions
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):
    # def convertToTitle_PRACTICE(self, n):
    def convertToTitle(self, n):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lst = []
        m = 1
        if n < 27:
            return alpha[n-1]
        while n > 1:
            if n < 26:
                lst.insert(0, alpha[(n % 26)-m])
            else:
                r = n % 26
                lst.insert(0, alpha[r-1])
            n //= 26
            m += 1

        return ''.join(lst)

    def convertToTitle_PASS(self, n):
    # def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while (n > 0):
            n -= 1
            r = chr(n & +65) + r
            n //= 26
        return r


def main():
    print(Solution().convertToTitle(1))       # A
    print(Solution().convertToTitle(2081))    # CBA
    print(Solution().convertToTitle(26))      # Z
    print(Solution().convertToTitle(27))      # AA
    print(Solution().convertToTitle(52))      # AZ
    print(Solution().convertToTitle(78))      # BZ
    print(Solution().convertToTitle(104))      #
    print(Solution().convertToTitle(130))      #
    print(Solution().convertToTitle(156))      #


# LC input
# 1
# 2081
# 26
# 27
# 52

if __name__ == '__main__':
    main()
