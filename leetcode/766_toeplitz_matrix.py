"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""
class Solution(object):
    # def isToeplitzMatrix_2(self, matrix):
    def isToeplitzMatrix(self, matrix):
        i = 1
        while i < len(matrix):
            j = 1
            while j < len(matrix[i]):
                if j-1 >= 0:
                    if matrix[i-1][j-1] != matrix[i][j]:
                        return False
                j += 1
            i += 1
        return True


    def isToeplitzMatrix_1(self, matrix):
    # def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m_len = len(matrix)
        row_len = len(matrix[0])

        if row_len < 2:
            return True

        i = 1
        j = 1
        while i < m_len:
            _this = matrix[i][j:]
            pre = matrix[i-1][j-1:-1]
            if _this != pre:
                return False

            if i < m_len-1:
                _this = matrix[i][j-1:-1]
                nxt = matrix[i+1][j:]
                if _this != nxt:
                    return False

            i += 1
            j += 1

        return True

def main():
    # True
    print(Solution().isToeplitzMatrix([[1,2,3,4],
                                       [5,1,2,3],
                                       [9,5,1,2]]
                                      ))
    # False
    print(Solution().isToeplitzMatrix([[11,74,0,93],
                                       [40,11,74,7]]
                                      ))

    # False
    print(Solution().isToeplitzMatrix([[11,74,0,93],
                                       [40,11,74,7],
                                       [40,74,11,7]]
                                      ))

    # False
    print(Solution().isToeplitzMatrix([[1,2],
                                       [2,1],
                                       [2,1]]
                                      ))
    #
    # # True
    print(Solution().isToeplitzMatrix([[18],
                                       [66]]
                                      ))
    #
    # True
    print(Solution().isToeplitzMatrix([[97,97],
                                       [80,97],
                                       [10,80]]
                                      ))

    # False
    print(Solution().isToeplitzMatrix([[41,45],
                                       [81,41],
                                       [73,81],
                                       [47,73],
                                       [0,47],
                                       [79,76]]
                                      ))


#LC input
# [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# [[11,74,0,93],[40,11,74,7]]
# [[11,74,0,93],[40,11,74,7],[40,74,11,7]]
# [[1,2],[2,1],[2,1]]
# [[18],[66]]
# [[97,97],[80,97],[10,80]]
# [[41,45],[81,41],[73,81],[47,73],[0,47],[79,76]]

if __name__ == '__main__':
    main()

