"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.
"""
class Solution(object):
    # def countNumbersWithUniqueDigits_PRACTICE(self, n):
    def countNumbersWithUniqueDigits(self, n):
        return

    def countNumbersWithUniqueDigits_SOL(self, n):
    # def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        prod = retval = 1
        for i in range(n if n <= 10 else 10):
            prod *= choices[i]
            retval += prod
        return retval



def main():
    print(Solution().countNumbersWithUniqueDigits(2))   # 91
    print(Solution().countNumbersWithUniqueDigits(3))   # 739
    print(Solution().countNumbersWithUniqueDigits(0))   # 1
    print(Solution().countNumbersWithUniqueDigits(7))   # 712891


if __name__ == '__main__':
    main()


"""
class Solution:
    def func(self):
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
