# Instructions
"""
Write an algorithm such that if an element in an MxN matrix is 0, it;'s entire row and column are set to 0
"""


class Solution():
    def zero_matrix(self, matrix):
        r_count = len(matrix)
        seen = {}
        for i in range(r_count):
            col_count = len(matrix[i])
            for j in range(col_count):
                visited = seen.get('{},{}'.format(i, j))
                if not visited and matrix[i][j] == 0:
                    x = r_count - 1
                    while x >= 0:
                        if matrix[x][j] != 0:
                            seen['{},{}'.format(x, j)] = True
                            matrix[x][j] = 0
                        x -= 1
                    y = len(matrix[i]) - 1
                    while y >= 0:
                        if matrix[i][y] != 0:
                            seen['{},{}'.format(i, y)] = True
                            matrix[i][y] = 0
                        y -= 1


def print_matrix(matrix):
    for r in matrix:
        print(r)


def main():
    matrix = [
        [0,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]]

    Solution().zero_matrix(matrix)
    print_matrix(matrix)
    print('=====================')

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 0, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
    ]

    Solution().zero_matrix(matrix)
    print_matrix(matrix)
    print('=====================')

    matrix = [[0,   2,  3,  4,  5,  6,  7,  8],
              [9,  10, 11, 12, 13, 14, 15, 16],
              [17, 18, 0, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 0, 30, 31, 32],
              [33, 0, 35, 36, 37, 38, 39, 40],
              [41, 42, 43, 44, 45, 46, 47, 48],
              [49, 50, 51, 0, 53, 54, 55, 56],
              [57, 58, 59, 60, 61, 0, 0, 64]]

    Solution().zero_matrix(matrix)
    print_matrix(matrix)
    print('=====================')


if __name__ == '__main__':
    main()