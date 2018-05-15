#!/usr/bin/python3
import random
import sys
from threading import Thread
import time

take_input = False


class Solution():
    def num_islands_PRACTICE(self, grid):
    # def num_islands(self, grid):
        return

    # def num_islands_PASSED(self, grid):
    def num_islands(self, grid):
        def helper(grid, i, j):
            if i > len(grid) - 1 or j > len(grid[i]) - 1 or i < 0 or j < 0 or grid[i][j] == '0':
                return 0

            grid[i][j] = '0'
            helper(grid, i, j+1)
            helper(grid, i+1, j)
            helper(grid, i, j-1)
            helper(grid, i-1, j)
            return 1

        retval = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                retval += helper(grid, i, j)
        return retval


def main():
    # expect: 1
    # print(Solution().num_islands([["1", "1", "1", "1", "0"],
    #                               ["1", "1", "0", "1", "0"],
    #                               ["1", "1", "0", "0", "0"],
    #                               ["0", "0", "0", "0", "0"]]))  # 1
    #
    # print(Solution().num_islands([["1", "1", "0", "1", "0"],
    #                               ["1", "1", "0", "1", "0"],
    #                               ["1", "1", "0", "0", "0"],
    #                               ["0", "0", "0", "0", "0"]]))  # 2
    #
    # print(Solution().num_islands([["1", "1", "0", "1", "0"],
    #                               ["1", "1", "0", "1", "0"],
    #                               ["1", "1", "0", "0", "0"],
    #                               ["0", "0", "0", "0", "1"]]))  # 3

    print(Solution().num_islands([["1", "0", "0", "1"],
                                  ["0", "0", "0", "1"],
                                  ["0", "0", "0", "1"],
                                  ]))  # 1


# LC Input
# [["1", "1", "1", "1", "0"],["1", "1", "0", "1", "0"],["1", "1", "0", "0", "0"],["0", "0", "0", "0", "0"]]
# [["1", "1", "0", "1", "0"],["1", "1", "0", "1", "0"],["1", "1", "0", "0", "0"],["0", "0", "0", "0", "0"]]
# [["1", "1", "0", "1", "0"],["1", "1", "0", "1", "0"],["1", "1", "0", "0", "0"],["0", "0", "0", "0", "1"]]

if __name__ == "__main__":
    main()
