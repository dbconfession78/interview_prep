from collections import defaultdict, Counter
test_no = 1
def n_queens(n):
    def has_no_diag(coord, placed):
        i = coord[0]
        j = coord[1]
        while i >= 0 and j >= 0:
            i -= 1
            j -= 1
            if (i, j) in placed:
                return False

        i = coord[0]
        j = coord[1]
        while i >= 0 and j < n:
            i -= 1
            j += 1
            if (i, j) in placed:
                return False
        return True

    stk = [((0, i), {(0, i)}, {j for j in range(n) if j != i}) for i in range(n)]
    perms = []
    retval = []
    while stk:
        curr, placed, cols = stk.pop(0)
        if len(placed) == n:
            if placed not in perms:
                perms.append(placed)
        x = curr[0]; y = curr[1]
        if x == n-1:
            continue
        for j in range(n):
            if (j < n and (j > y + 1)) or (j >= 0 and (j < y - 1)):
                if j in cols  and has_no_diag((x+1, j), placed):
                    new_tuple = ((x+1, j), placed.union({(x+1, j)}), cols - {j})
                    stk.append(new_tuple)


    for perm in perms:
        ret = [0 for _ in range(n)]
        for coord in perm:
            col = coord[1]
            row = coord[0]+1
            ret[col] = row
        # print_board(perm, n)
        retval.append(ret)
    return sorted(retval)


def print_board(placed, n):
    board = [["-" for _ in range(n)] for x in range(n)]
    for cell in placed:
        i = cell[0]
        j = cell[1]
        board[i][j] = "X"
    for row in board:
        print(row)
    print("=============")


def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))


def main():
    ######### TESTS ############
    test(1, n_queens(1))
    test([[2,4,1,3],[3,1,4,2]], n_queens(4))
    test([], n_queens(2))
    test([], n_queens(3))
    test([[2,4,6,1,3,5], [3,6,2,5,1,4], [4,1,5,2,6,3], [5,3,1,6,4,2]], n_queens(6))

if __name__ == "__main__":
    main()

