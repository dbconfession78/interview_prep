"""
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:

Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
"""

from bisect import bisect
class Solution():
    def Descending_Order(self, num):
        str_num = str(num)
        return int(''.join(sorted([x for x in str_num])[::-1]))





def main():
    print(Solution().Descending_Order(21445))       # 54421
    print(Solution().Descending_Order(145263))      # 654321
    print(Solution().Descending_Order(1254859723))  # 9875543221



if __name__ == '__main__':
    main()