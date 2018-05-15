# Instructions
"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""

from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = defaultdict(int)
        odd_count = 0
        for c in s:
            dct[c] += 1
            if dct[c] % 2 != 0:
                odd_count += 1
            else:
                odd_count -= 1

        return False if odd_count > 1 else True




def main():
    print(Solution().canPermutePalindrome('aab'))   # True


if __name__ == '__main__':
    main()
