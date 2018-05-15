import sys

class Solution:
    # from leetcode discussion 722 ms
    # def islandPerimeter_PRACTICE(self, grid):
    def islandPerimeter(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return self.helper(grid, i, j, 0)

    def helper(self, grid, i, j, retval):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1 or grid[i][j] == 0:
            return retval + 1
        if grid[i][j] == 2:
            return retval

        grid[i][j] = 2
        retval = self.helper(grid, i, j - 1, retval)
        retval = self.helper(grid, i - 1, j, retval)
        retval = self.helper(grid, i, j + 1, retval)
        retval = self.helper(grid, i + 1, j, retval)

        return retval

    def islandPerimeter_PASSED(self, grid):
    # def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def sum_adjacent(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count

    # mine 1045 ms
    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 1:
                    return self.helper2(grid, i, j)
        return 0

    def helper2(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return 0
        if grid[i][j] == 0 or grid[i][j] == 'X':
            return 0
        grid[i][j] = 'X'

        perim = self.count_perim(grid, i, j)
        perim += self.helper2(grid, i, j + 1)
        perim += self.helper2(grid, i, j - 1)
        perim += self.helper2(grid, i + 1, j)
        perim += self.helper2(grid, i - 1, j)

        return perim

    def count_perim(self, grid, i, j):
        perim = 0
        if i == 0:
            perim += 1
        if i == len(grid) - 1:
            perim += 1
        if j == 0:
            perim += 1
        if j == len(grid[0]) - 1:
            perim += 1

        if j < len(grid[0])-1:
            if grid[i][j + 1] == 0:
                perim += 1

        if j > 0:
            if grid[i][j - 1] == 0:
                perim += 1

        if i < len(grid) - 1:
            if grid[i + 1][j] == 0:
                perim += 1

        if i > 0:
            if grid[i - 1][j] == 0:
                perim += 1
        return perim


def main():
    """Test cases"""

    # 16
    print(Solution().islandPerimeter([
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]))

    # 24
    print(Solution().islandPerimeter([
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 0, 0]
    ]))

    # 4
    print(Solution().islandPerimeter([[1]]))

    # for row in grid:
    #     for i, col in enumerate(row):
    #         if col == 1:
    #             sys.stdout.write(str(col))
    #         else:
    #             sys.stdout.write('-')
    #         sys.stdout.write(' ')
    #         if i == len(row) - 1:
    #             print()

# LC Input
# [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# [[0, 1, 0, 0],[1, 1, 1, 1],[0, 1, 0, 0],[1, 1, 0, 0],[1, 1, 1, 0],[1, 1, 0, 0]]
# [[1]]


if __name__ == '__main__':
    main()

# Instructions
"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
https://leetcode.com/static/images/problemset/island.png

"""