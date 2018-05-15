# 37. Sudoku Solver
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
"""

from collections import Counter
import random
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # print_board(board)
        memo = {}
        print_board(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    if i < 3 and j < 3:
                        sub_id = 1
                    elif i < 3 and (j >= 3 and j < 6):
                        sub_id = 2
                    elif i < 3 and (j >= 6 and j < 9):
                        sub_id = 3
                    elif (i >= 3 and i < 6) and (j < 3):
                        sub_id = 4
                    elif (i >=3 and i < 6) and (j >= 3 and j < 6):
                        sub_id = 5
                    elif (i >=3 and i < 6) and (j >= 6 and j < 9):
                        sub_id = 6
                    elif (i >= 6 and i < 9) and (j < 3):
                        sub_id = 7
                    elif (i >= 6 and i < 9) and (j >= 3 and j < 6):
                        sub_id = 8
                    elif (i >= 6 and i < 9) and (j >= 6 and j < 9):
                        sub_id = 9


                    cache = memo.get('{},{},{}'.format(i, j, sub_id))
                    if cache:
                        col_avail = cache[0]
                        row_avail = cache[1]
                        sub_avail = cache[2]
                    else:
                        col_avail = self.get_avail_in_col(board, j)
                        row_avail = self.get_avail_in_row(board, i)
                        sub_avail = self.get_avail_in_sub(board, sub_id)
                        memo['{},{},{}'.format(i, j, sub_id)] = [col_avail, row_avail, sub_avail]

                    combine = Counter(col_avail + row_avail + sub_avail)
                    avail_for_cell = [k for k, v in combine.items() if v == 3]
                    to_use = random.choice(avail_for_cell)
                    del(col_avail[col_avail.index(to_use)])
                    del(row_avail[row_avail.index(to_use)])
                    del(sub_avail[sub_avail.index(to_use)])
                    memo['{},{},{}'.format(i, j, sub_id)] = [col_avail, row_avail, sub_avail]
                    board[i][j] = str(to_use)
                    print_board(board)
                    print()
                    print()

    def get_avail_in_col(self, board, j):
        nums = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        i = 0
        while i < len(board):
            cell = board[i][j]
            if cell != '.':
                nums[int(board[i][j])] += 1
            i += 1
        avail = [k for k, v in nums.items() if v == 0]
        return avail

    def get_avail_in_row(self, board, i):
        nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        j = 0
        while j < len(board[i]):
            cell = board[i][j]
            if cell != '.':
                nums[int(board[i][j])] += 1
            j += 1
        avail = [k for k, v in nums.items() if v == 0]
        return avail

    def get_avail_in_sub(self, board, sub_id):
        nums = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        sub_board = self.get_sub_board(board, sub_id)
        for i in range(3):
            for j in range(3):
                cell = sub_board[i][j]
                if cell != '.':
                    nums[int(cell)] += 1
        avail = [k for k, v in nums.items() if v == 0]
        return avail

    def get_sub_board(self, board, sub_board_id):
        dct = {1:[board[0][0:3], board[1][0:3], board[2][0:3]],
               2: [board[0][3:6], board[1][3:6], board[2][3:6]],
               3: [board[0][6:9], board[1][6:9], board[2][6:9]],
               4: [board[3][0:3], board[4][0:3], board[5][0:3]],
               5: [board[3][3:6], board[4][3:6], board[5][3:6]],
               6: [board[3][6:9], board[4][6:9], board[5][6:9]],
               7: [board[6][0:3], board[7][0:3], board[8][0:3]],
               8: [board[6][3:6], board[7][3:6], board[8][3:6]],
               9: [board[6][6:9], board[7][6:9], board[8][6:9]]}

        sub_board = dct[sub_board_id]
        # for row in sub_board:
        #     print(row)
        return sub_board

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i = 0
        if not self.rows_are_valid(board):
            return False
        if not self.cols_are_valid(board):
            return False
        while i < len(board):
            j = 0
            while j < len(board):
                if not self.sub_box_is_valid(board, i, j):
                    return False
                j += 3
            i += 3
        return True

    def rows_are_valid(self, board):
        for row in board:
            counter = Counter()
            for cell in row:
                if cell != '.':
                    if counter.get(cell) == 1:
                        return False
                    counter[cell] += 1
        return True

    def cols_are_valid(self, board):
        """
        checks to see if all rows contain only 1
        :param board: the board to check
        :return: True if all rows are valid
        """
        for j in range(9):
            counter = Counter()
            for i in range(9):

                cell = board[i][j]
                if cell != '.':
                    if counter.get(cell) or not cell.isdigit() or cell == '0':
                        return False
                    counter[board[i][j]] += 1
        return True

    def sub_box_is_valid(self, board, i, j):
        counter = Counter()
        sub_box = [board[i][j: j+3], board[i+1][j: j+3], board[i+2][j:j+3]]
        for row in sub_box:
            for cell in row:
                if cell != '.':
                    if counter.get(cell) and counter.get(cell) == 1:
                        return False
                    counter[cell] += 1
        return True


def print_board(board):
    for row in board:
        print(row)

def main():
    print(Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))


# expected
#[
# ["5","1","9","7","4","8","6","3","2"],
# ["7","8","3","6","5","2","4","1","9"],
# ["4","2","6","1","3","9","8","7","5"],
# ["3","5","7","9","8","6","2","4","1"],
# ["2","6","4","3","1","7","5","9","8"],
# ["1","9","8","5","2","4","3","6","7"],
# ["9","7","5","8","6","3","1","2","4"],
# ["8","3","2","4","9","1","7","5","6"],
# ["6","4","1","2","7","5","9","8","3"]
# ]

if __name__ == '__main__':
    main()