# Integer to Roman
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # def intToRoman_PRACTICE(self, num):
    def intToRoman(self, num):
        INTS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ROMS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        retval = ""
        for i, x in enumerate(INTS):
            x = num // INTS[i]
            retval += (ROMS[i] * x)
            num = num % INTS[i]
        return retval



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
    print(Solution().intToRoman(1))     # "I"
    print(Solution().intToRoman(567))   # "DLXVII"
    print(Solution().intToRoman(3999))  # "MMMCMXCIX"
    print(Solution().intToRoman(2))     # "II"

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