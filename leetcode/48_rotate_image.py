# Instructions
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        _len = len(matrix)
        last = _len - 1
        lay_count = _len // 2 if (_len % 2 == 0) else (_len // 2) + 1
        mid = last // 2
        for lay in range(lay_count):
            lay_lst = self.get_layer(matrix, lay, mid, last)
            self.write_layer(matrix, lay_lst, lay)
        return matrix

    def write_layer(self, matrix, lay_lst, lay):
        _len = len(matrix)
        last = _len - 1
        if len(lay_lst) == 1:
            return

        top = lay_lst[0]
        right = lay_lst[1]
        bottom = lay_lst[2]
        left = lay_lst[3]
        lst = left[::-1][:-1]+top[:-1]+right[:-1]+bottom[::-1][:-1]

        # top
        for i in range(last-(lay*2)):
            matrix[lay][i+lay] = lst.pop(0)

        # right
        for i in range(last-(2*lay)):
            matrix[i+lay][last-lay] = lst.pop(0)

        # bottom
        i = last-lay
        while lst and i > lay:
            matrix[last-lay][i] = lst.pop(0)
            i -= 1

        # left
        if lst:
            i = last-lay
            while lst and i > lay:
                matrix[i][lay] = lst.pop(0)
                i -= 1

    def get_layer(self, matrix, lay, mid, last):
        _len = len(matrix)
        last = _len - 1
        if lay == _len // 2:
            if _len % 2 != 0:
                # print([matrix[lay][lay]])
                return [[matrix[lay][lay]]]
        top = matrix[lay][lay:_len-lay]
        right = [x[_len-lay-1] for x in matrix[lay:_len-lay]]
        bottom = matrix[last-lay][lay:_len-lay]
        left = [x[lay] for x in matrix[lay:_len-lay]]

        layer = [top, right, bottom, left]
        return layer


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def main():

    # 21, 16, 11, 6,   1
    # 22, 17, 12, 7,   2
    # 23, 18, 13, 8,   3
    # 24, 19, 14, 9,   4
    # 25, 20, 15, 10,  5
    # print_matrix(Solution().rotate([[1,   2,  3,  4,   5],
    #                                 [6,   7,  8,  9,  10],
    #                                 [11, 12, 13, 14,  15],
    #                                 [16, 17, 18, 19,  20],
    #                                 [21, 22, 23, 24,  25]
    #                                 ]))

    # 7, 4, 1
    # 8, 5, 2
    # 9, 6, 3
    # print_matrix(Solution().rotate([[1,2,3],
    #                                 [4,5,6],
    #                                 [7,8,9]
    #                                 ]))

    # 15, 13, 2,  5
    # 14,  3, 4,  1
    # 12,  6, 8,  9
    # 16, 7, 10, 11
    # print_matrix(Solution().rotate([[ 5, 1, 9,11],
    #                                 [ 2, 4, 8,10],
    #                                 [13, 3, 6, 7],
    #                                 [15,14,12,16]
    #                                 ]))

    #  4, 33, 13, 32, 12,  2
    # 24,  1, 14, 33, 27, 29
    # 1,  20, 32, 32,  9, 20
    # 6,   7, 27,  2, 25, 26
    # 32, 21, 22, 28, 13, 16
    # 34,  7, 26, 14, 21, 28
    # print_matrix(Solution().rotate([[2,29,20,26,16,28],
    #                                 [12,27,9,25,13,21],
    #                                 [32,33,32,2,28,14],
    #                                 [13,14,32,27,22,26],
    #                                 [33,1,20,7,21,7],
    #                                 [4,24,1,6,32,34]
    #                                 ]))

    expected = [[12, 29, 28, 18, 14,  9, 43],
    [23, 45, 44, 31, 42, 18, 39],
    [35, 33, 14, 45,  3,  9,  3],
    [32, 45, 23, 11, 23, -1, 33],
    [22, 20, 40,  8, 12, 40, 37],
    [39,  0, 24, -1, 14, 22, 20],
    [8, 45, 13, 31, 32, 38, 14]]
    ans = Solution().rotate([[43,39,3,33,37,20,14],
                                    [9,18,9,-1,40,22,38],
                                    [14,42,3,23,12,14,32],
                                    [18,31,45,11,8,-1,31],
                                    [28,44,14,23,40,24,13],
                                    [29,45,33,45,20,0,45],
                                    [12,23,35,32,22,39,8]])
    print_matrix(ans)
    print(ans == expected)



# LC input
# [[1,2,3],[4,5,6],[7,8,9]]
# [[1,2,3,4,5],[6,7,8,9,10][11,12,13,14,15][16,17,18,19,20],[21,22,23,24,25]]
# [[1,2,3],[4,5,6],[7,8,9]]
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
# [[43,39,3,33,37,20,14],[9,18,9,-1,40,22,38],[14,42,3,23,12,14,32],[18,31,45,11,8,-1,31],[28,44,14,23,40,24,13],[29,45,33,45,20,0,45],[12,23,35,32,22,39,8]]

if __name__ == '__main__':
    main()