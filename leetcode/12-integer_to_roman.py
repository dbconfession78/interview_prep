# Integer to Roman
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
from sgk_test import test
class Solution:
    # def intToRoman_PRACTICE(self, num):
    def intToRoman(self, num):
        return



    def intToRoman_PASSED(self, num):
    # def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        INTS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ROMANS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        ret = ""
        i = 0
        while num:
            ret += (num // INTS[i]) * ROMANS[i]
            num %= INTS[i]
            i += 1
        return ret


def main():
    test("I", Solution().intToRoman(1))
    test("DLXVII", Solution().intToRoman(567))
    test("MMMCMXCIX", Solution().intToRoman(3999))
    test("II", Solution().intToRoman(2))
    test("IV", Solution().intToRoman(4))

# LC input
# 1
# 567
# 3999

if __name__ == '__main__':
    main()

#Instructions:
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.


"""