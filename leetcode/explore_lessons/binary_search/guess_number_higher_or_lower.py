"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# *** when pasting into LC, remove 2nd param, 'tgt' from method def and calls

class Solution(object):
    def guessNumber(self, n, tgt):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            m = left + (right - left) // 2
            res = guess(m, tgt)
            if res == 0:
                return m
            elif res == -1:
                right = m - 1
            else:
                left = m + 1


def guess(g, tgt=6):
    if g == tgt:
        return 0
    return -1 if tgt < g else 1


def main():
    print(Solution().guessNumber(10, tgt=6))

# *** when pasting into LC, remove 2nd param, 'tgt' from method def and calls


if __name__ == '__main__':
    main()
