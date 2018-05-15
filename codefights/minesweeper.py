def minesweeper(matrix):
    retval = []
    i = 0
    while i < len(matrix):
        j = 0
        row = []
        while j < len(matrix[i]):
            row.append(get_pos_sum(i, j, matrix))
            j += 1
        retval.append(row)
        i += 1
    return retval


def get_pos_sum(i, j, matrix):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    sum = 0
    for dir in dirs:
        v, h = dir

        if (v + i) >= 0 and (v + i) < len(matrix) and (h + j) >= 0 and (h + j) < len(matrix[i]):
            sum += matrix[v + i][h + j]

    return sum


def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
   retval = minesweeper([
       [True,False,False,True],
       [False,False,True,False],
       [True,True,False,True]
   ])
   test(retval,
        [[0,2,2,1],
         [3,4,3,3],
         [1,2,3,1]])

if __name__ == '__main__':
    main()