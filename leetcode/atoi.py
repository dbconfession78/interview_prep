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


s = '-++--01234567890000abc'
#s = '+'
s = '-2'
s = '   010'
s = '1'
s = "    -00134"
s = '+-2'
s = "  -0012a42"
s = "    +0a32"
s = "     2147483648"
s = ''
print(s)
sol = Solution().atoi(s)
print(sol)
