def construct_pascals_trigangle(n):
    """
    construct_pascals_trigangle - builds a Pascal triangle n levels in height
    :param n: height of triangle
    :return: 2d array-list containing completed triangle
    """
    retval = [[1], [1, 1]]
    for i in range(1, n-1):
        new_row = build_row(retval[i])
        retval.append(new_row)
    return retval


def build_row(prev_row):
    """
    build_row - builds a Pascal Triangle row.
    :param prev_row: array-list whose values are used to calculate new row
    :return: array-list containing values of new row
    """
    retval = []
    for i in range(len(prev_row) - 1):
        s = prev_row[i] + prev_row[i + 1]
        retval.append(s)
    return [1] + retval + [1]


class Test:
    def __init__(self):
        self.test_no = 1

    def test(self, expected, actual):
        print("{}. ".format(self.test_no), end="")
        self.test_no += 1
        if actual != expected:
            print("FAIL", end=" ")
        else:
            print("OK", end=" ")
        print(" - sol: {},  ret: {}".format(expected, actual))


def main():
    ######### TESTS ############
    t = Test()
    t.test([[1],
            [1, 1]], construct_pascals_trigangle(2))

    t.test([[1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]], construct_pascals_trigangle(4))

    t.test([[1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]], construct_pascals_trigangle(5))

    t.test([[1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1]], construct_pascals_trigangle(8))


if __name__ == "__main__":
    main()
