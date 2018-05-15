# 461. Hamming Distance
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
https://en.wikipedia.org/wiki/Hamming_distance

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

class Solution:
    # def hammingDistance_PRACTICE(self, x, y):
    def hammingDistance(self, x, y):
        return

    def hammingDistance_PASSED(self, x, y):
    # def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        retval = 0
        while xor > 0:
            if ((xor >> 1) << 1) != xor:
                retval += 1
            xor >>= 1
        return retval



def main():
    print(Solution().hammingDistance(1,4))  # 2


if __name__ == '__main__':
    main()

