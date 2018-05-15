# Instructions
"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
class Solution(object):
    # def hammingWeight_PRACTICE(self, n):
    def hammingWeight(self, n):
        return

    def hammingWeight_PASSED(self, n):
    # def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        retval = 0
        while n > 0:
            if n & 1:
                retval += 1
            n >>= 1
        return retval


def main():
    print(Solution().hammingWeight(1))  # 1
    print(Solution().hammingWeight(2))  # 1
    print(Solution().hammingWeight(3))  # 2


if __name__ == '__main__':
    main()