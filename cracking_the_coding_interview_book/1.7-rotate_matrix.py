# Instructions
"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""


class Solution():
    def rotate_matrix(self, matrix):
        _len = len(matrix)
        if _len != len(matrix[0]):
            return False
        for layer in range(_len//2):
            self.rotate_layer(matrix, layer)

    def rotate_layer(self, matrix, layer):
        row_len = len(matrix) - (2 * layer)
        top = matrix[layer][layer:row_len+layer]
        right = [x[-1-layer] for x in matrix[layer:row_len+layer]]
        bottom = [x for x in matrix[-1-layer][layer:row_len+layer]]
        left = [x[layer] for x in matrix[layer:row_len+layer]]

        lst = top[:-1] + right[:-1] + bottom[::-1][:-1] + left[::-1][:-1]

        # top
        i = 0
        while i < row_len-1:
            p = lst.pop()
            matrix[layer][-2-i-layer] = p
            i += 1

        # left
        i = 1
        while i < row_len-1:
            p = lst.pop()
            matrix[layer+i][0+layer] = p
            i += 1

        # bottom
        i = 0
        while i < row_len-1:
            p = lst.pop()
            matrix[-1-layer][i+layer] = p
            i += 1

        # right
        i = 0
        while i < row_len:
            p = lst.pop()
            matrix[-1-i-layer][-1-layer] = p
            i += 1

        return True


    def rotate_matrix_BOOK(self, matrix):
        print_matrix(matrix)
        print('-------------')
        _len = len(matrix)
        if _len == 0 or _len != len(matrix[0]):
            return False
        layer = 0
        while layer < _len // 2:
            first = layer
            last = _len - 1 - layer
            i = first
            while i < last:
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top

                i += 1
            layer += 1
        print_matrix(matrix)
        return True
    # def rotate_matrix(self, matrix):
        print_matrix(matrix)
        print('-------------')
        _len = len(matrix)
        if _len == 0 or _len != len(matrix[0]):
            return False
        layer = 0
        while layer < _len // 2:
            first = layer
            last = _len - 1 - layer
            i = first
            while i < last:
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top

                i += 1
            layer += 1
        print_matrix(matrix)
        return True

def print_matrix(matrix):
    for r in matrix:
        print(r)


def main():
    var = tuple()
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

    Solution().rotate_matrix(matrix)
    print_matrix(matrix)
    print('=====================')

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

    Solution().rotate_matrix(matrix)
    print_matrix(matrix)
    print('=====================')

    matrix = [[x for x in range(1, 9)],
        [x for x in range(9, 17)],
        [x for x in range(17, 25)],
        [x for x in range(25, 33)],
        [x for x in range(33, 41)],
        [x for x in range(41, 49)],
        [x for x in range(49, 57)],
        [x for x in range(57, 65)]]

    Solution().rotate_matrix(matrix)
    print_matrix(matrix)
    print('=====================')
    # [1,   2,  3,  4,  5,  6,  7,  8]
    # [9,  10, 11, 12, 13, 14, 15, 16]
    # [17, 18, 19, 20, 21, 22, 23, 24]
    # [25, 26, 27, 28, 29, 30, 31, 32]
    # [33, 34, 35, 36, 37, 38, 39, 40]
    # [41, 42, 43, 44, 45, 46, 47, 48]
    # [49, 50, 51, 52, 53, 54, 55, 56]
    # [57, 58, 59, 60, 61, 62, 63, 64]

    matrix = [[43,39,3,33,37,20,14],
                                    [9,18,9,-1,40,22,38],
                                    [14,42,3,23,12,14,32],
                                    [18,31,45,11,8,-1,31],
                                    [28,44,14,23,40,24,13],
                                    [29,45,33,45,20,0,45],
                                    [12,23,35,32,22,39,8]]

    Solution().rotate_matrix(matrix)
    print_matrix(matrix)
    print('=====================')

if __name__ == '__main__':
    main()