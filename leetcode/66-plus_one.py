# Instructions
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution:
    # def plusOne_PRACTICE(self, digits):
    def plusOne(self, digits):
        return


    def plusOne_PASSED(self, digits):
    # def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        _len = len(digits)
        i = _len - 1
        carry = 1
        while i > 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1
        digits[i] += carry

        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)

        return digits



def main():
    print(Solution().plusOne([0]))
    print(Solution().plusOne([9,9,9]))
    print(Solution().plusOne([9,9,9,9,6,9,9]))

# LC input
# [0]
# [9,9,9]
# [9,9,9,9,6,9,9]

if __name__ == '__main__':
    main()
