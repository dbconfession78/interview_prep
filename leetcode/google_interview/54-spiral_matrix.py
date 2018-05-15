class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        retlist = []
        while matrix:
            retlist += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                   retlist.append(row.pop())
            if matrix and matrix[0]:
                retlist += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    retlist.append(row.pop(0))
        return retlist






def main():
    print(Solution().spiralOrder([[1, 2, 3]
[4, 5, 6]
[7, 8, 9]]))
    print(Solution().spiralOrder([[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 16]]))


if __name__ == '__main__':
    main()