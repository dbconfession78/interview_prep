class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n % 4 == 0) == 0

def main():
    print(Solution().canWinNim(1))
    print(Solution().canWinNim(2))
    print(Solution().canWinNim(3))
    print(Solution().canWinNim(4))
    print(Solution().canWinNim(5))
    print(Solution().canWinNim(6))
    print(Solution().canWinNim(7))
    print(Solution().canWinNim(8))
    print(Solution().canWinNim(9))
    print(Solution().canWinNim(10))
    print(Solution().canWinNim(11))
    print(Solution().canWinNim(12))
    print(Solution().canWinNim(13))
    print(Solution().canWinNim(14))
    print(Solution().canWinNim(15))
    print(Solution().canWinNim(16))



if __name__ == '__main__':
    main()

# Instructions
"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""