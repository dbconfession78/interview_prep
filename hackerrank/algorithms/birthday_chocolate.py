# Birthday Chocolate

def solve(squares, day, month):
    retval = 0
    i = 0

    if len(squares) == 0:
        return 0
    if len(squares) == 1:
        if month != 1:
            return 0
        if squares[0] == day:
            return 1
        return 0

    while i < len(squares):
        if sum(squares[i:i + month]) == day:
            retval += 1
        i += 1
    return retval



print(solve([1,2,3,4], 4, 2))