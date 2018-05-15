"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char grid

A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

[output] boolean

Return true if grid represents a valid Sudoku puzzle, otherwise return false.
"""


def sudoku2(grid):
    if not all_cols_valid(grid) or not all_blocks_valid(grid) or not all_rows_valid(grid):
        return False
    return True


def all_rows_valid(grid):
    for row in grid:
        if not is_valid_row(row):
            return False
    return True

def is_valid_row(row):
    seen = set()
    for elem in row:
        if elem in seen:
            return False
        if elem != ".":
            seen.add(elem)
    return True


def all_blocks_valid(grid):
    block_1 = grid[0][0:3] + grid[1][0:3] + grid[2][0:3]
    block_2 = grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
    block_3 = grid[0][6:9] + grid[1][6:9] + grid[2][6:9]

    block_4 = grid[3][0:3] + grid[4][0:3] + grid[5][0:3]
    block_5 = grid[3][3:6] + grid[4][3:6] + grid[5][3:6]
    block_6 = grid[3][6:9] + grid[4][6:9] + grid[5][6:9]

    block_7 = grid[6][0:3] + grid[7][0:3] + grid[8][0:3]
    block_8 = grid[6][3:6] + grid[7][3:6] + grid[8][3:6]
    block_9 = grid[6][6:9] + grid[7][6:9] + grid[8][6:9]
    blocks = [block_1] + [block_2] + [block_3] + [block_4] + [block_5] + [block_6] + [block_7] + [block_8] + [block_9]
    for block in blocks:
        if not is_valid_block(block):
            return False
    return True

def is_valid_block(block):
    seen = set()
    for i in range(len(block)):
        if block[i] in seen:
            return False
        if block[i] != ".":
            seen.add(block[i])
    return True


def all_cols_valid(grid):
    for i in range(len(grid)):
        if not is_valid_col(i, grid):
            return False
    return True


def is_valid_col(col_num, grid):
    col = [row[col_num] for row in grid if row[col_num] != "."]
    seen = set()
    for elem in col:
        if elem in seen:
            return False
        if elem != ".":
            seen.add(elem)
    return True

def main():
    print(sudoku2([
        [".",".",".","1","4",".",".","2","."],
        [".",".","6",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".","1",".",".",".",".",".","."],
        [".","6","7",".",".",".",".",".","9"],
        [".",".",".",".",".",".","8","1","."],
        [".","3",".",".",".",".",".",".","6"],
        [".",".",".",".",".","7",".",".","."],
        [".",".",".","5",".",".",".","7","."]]))


if __name__ == '__main__':
    main()