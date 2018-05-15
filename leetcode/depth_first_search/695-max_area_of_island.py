import sys

class Solution:
    # def maxAreaOfIsland_PRACTICE(self, grid):
    def maxAreaOfIsland(self, grid):
        retval = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    retval = max(retval, self.helper(grid, i, j, 0))
        return retval

    def helper(self, grid, i, j, area):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[i]) - 1 or grid[i][j] == 0:
            return area

        grid[i][j] = 0
        area += 1
        area = self.helper(grid, i, j + 1, area)
        area = self.helper(grid, i + 1, j, area)
        area = self.helper(grid, i, j - 1, area)
        area = self.helper(grid, i - 1, j, area)
        return area

    def maxAreaOfIsland_PASSED(self, grid):
    # def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        big = 0
        i = j = 0

        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == 1:
                    big = max(big, self.explore(grid, i, j))
                j += 1
            i += 1

        return big

    def explore(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1 or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        count = 1

        count += self.explore(grid, i, j + 1)
        count += self.explore(grid, i, j - 1)
        count += self.explore(grid, i - 1, j)
        count += self.explore(grid, i + 1, j)
        return count


def print_map(grid):
    for row in grid:
        for cell in row:
            sys.stdout.write('{} '.format(cell))

        print()


def main():

    # 4
    print(Solution().maxAreaOfIsland([
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]))

    # 3
    print(Solution().maxAreaOfIsland([
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]
    ]))

    # 1
    print(Solution().maxAreaOfIsland(([[1]])))


    # 6
    print(Solution().maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]))



# LC Input
# [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
# [[1]]
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

if __name__ == '__main__':
    main()


# Instructions
"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""