"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.

Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
from sgk_test import test
class Solution:
    # def atoi_PRACTICE(self, str):
    def atoi(self, str):
        return


    def atoi_PASSED(self, str):
    # def atoi(self, str):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -INT_MAX - 1

        chars = list(str)
        orig_len = len(chars)
        leading_blank_count = 0
        is_neg = False
        retval = None
        if orig_len == 0 or chars == [" " for _ in range(orig_len)]:
            return 0
        while chars[0] == " ":
            leading_blank_count += 1
            chars.pop(0)

        _len = orig_len - leading_blank_count
        if chars[0] in ("+", "-"):
            if chars[0] == "-":
                is_neg = True
            chars.pop(0)
            _len -= 1

        if _len == 0 or not chars[0].isdigit():
            return 0

        for i in range(_len):
            if i == _len - 1 or not chars[i + 1].isdigit():
                retval = int("".join(chars[:i + 1]))
                break

        if is_neg:
            retval *= -1

        if retval < INT_MIN:
            return INT_MIN

        if retval > INT_MAX:
            return INT_MAX

        return retval


test(0, Solution().atoi(''))
test(0, Solution().atoi("words and 987"))
test(3, Solution().atoi("3.14159"))
test(0, Solution().atoi(".1"))
test(123, Solution().atoi("123"))
test(0, Solution().atoi("0"))
test(-123, Solution().atoi("-123"))
test(0, Solution().atoi('-++--01234567890000abc'))
test(0, Solution().atoi('+'))
test(-2, Solution().atoi('-2'))
test(10, Solution().atoi('   010'))
test(1, Solution().atoi('1'))
test(-134, Solution().atoi('    -00134'))
test(0, Solution().atoi('+-2'))
test(-12, Solution().atoi('  -0012a42'))
test(0, Solution().atoi('    +0a32'))
test(2147483647, Solution().atoi('     2147483648'))
test(-4, Solution().atoi('   -04f'))



#LC input
# ""
# "123"
# "0"
# "-123"
# "-++--01234567890000abc"
# "+"
# "-2"
# "   010"
# "1"
# "    -00134"
# "+-2"
# "  -0012a42"
# "    +0a32"
# "     2147483648"




