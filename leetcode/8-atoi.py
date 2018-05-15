#!/usr/bin/python3
class Solution:
    def atoi(self, str):
        is_neg = False
        retval = 0
        nums = []
        factor = 1
        # 0-9 as string is  48-57 in ASCII

        str = str.strip()
        if str.startswith('-') or str.startswith('+'):
            if str.startswith('-'):
                is_neg = True
                str = str[1:]
            else:
                is_neg = False
                str = str[1:]

        if len(str) == 0:
            return 0
        first = ord(str[0])
        if first < 48 or first > 57:
            return 0

        for i in range(len(str)):
            conv = (ord(str[i]) - 48)
            if conv <= 9 and conv >= 0:
                nums.append(conv)
            else:
                break
        if len(nums) == 0:
            return 0

        while len(nums) > 0 and nums[0] == 0:
            nums.pop(nums.index(0))
        nums.reverse()
        for (i, num) in enumerate(nums):
            retval += num * factor
            factor *= 10

        if is_neg:
            retval *= -1
        return retval


# print(Solution().atoi(''))
# print(Solution().atoi("123"))
# print(Solution().atoi("0"))
# print(Solution().atoi("-123"))
# print(Solution().atoi('-++--01234567890000abc'))
# print(Solution().atoi('+'))
# print(Solution().atoi('-2'))
# print(Solution().atoi('   010'))
# print(Solution().atoi('1'))
# print(Solution().atoi('    -00134'))
print(Solution().atoi('+-2'))
print(Solution().atoi('  -0012a42'))
print(Solution().atoi('    +0a32'))
print(Solution().atoi('     2147483648'))
print(Solution().atoi('   -04f'))


# expected

# 0
# 123
# 0
# -123
# 0
# 0
# -2
# 10
# 1
# -134
# 0
# -12
# 0
# 2147483647

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




