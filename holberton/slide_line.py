from sgk_test import test
def slide_line(d, str):
    line = str.split(' ')
    line = [int(x) for x in line]
    size = len(line)
    if (line is None):
        return 0

    if (d == "L"):
        return (slide_left(line, size))
    if (d == "R"):
        return (slide_right(line, size))
    return 0

def slide_left(line, size):
    searching = 0
    mark = -1
    i = 0
    while i < size:
        if line[i] == 0:
            if searching == 0:
                searching = 1
                if mark == -1:
                    mark = i
        elif searching == 1:
            searching = 0
            if i < (size - 1):
                # next_idx = get_idx_of_next_non_zero(line, i + 1, size, 1)
                next_idx = get_idx_of_next_non_zero(line, i, size, 1)
                ret = merge(mark, i, line, next_idx, 1)
                i = ret[0]
                mark = ret[1]
                line = ret[2]
            else:
                line[mark] = line[i]
                line[i] = 0
        else:
            if i < (size - 1):
                next_idx =  get_idx_of_next_non_zero(line, i + 1, size, 1)
                ret = merge(mark, i, line, next_idx, 1)
                i = ret[0]
                mark = ret[1]
                line = ret[2]
        i += 1

    if i >= (size - 1):
        if mark > -1 and line[mark] == 0:
            line[mark] = line[size-1]
            line[size-1] = 0
    return line

def slide_right(line, size):
    searching = 0; mark = size;
    i = size - 1
    while i >= 0:
    # for (i = ((int) size - 1); i >= 0; i--)
        if line[i] == 0:
            if searching == 0:
                searching = 1
                if mark == size:
                    mark = i
        elif searching == 1:
            searching = 0
            if i > 0:
                next_idx =  get_idx_of_next_non_zero(line, i - 1, size, 2)
                ret = merge(mark, i, line, next_idx, 2)
                i = ret[0]
                mark = ret[1]
                line = ret[2]
            else:
                line[mark] = line[i]
                line[i] = 0
        else:
          if i > 0:
              next_idx =  get_idx_of_next_non_zero(line, i - 1, size, 2)
              ret = merge(mark, i, line, next_idx, 2)
              i = ret[0]
              mark = ret[1]
              line = ret[2]
        i -= 1
    if mark != size:
        line[mark] = line[i + 1]; line[i + 1] = 0
    return line

def merge(mark, i, line, next_idx, direction):
    size = len(line)
    if direction == 1:
        if next_idx > -1:
            if line[next_idx] == line[i]:
                if mark != -1:
                    line[mark] = line[i] + line[next_idx]
                    line[i] = 0
                    mark = mark + 1
                else:
                    line[i] = line[i] + line[next_idx]
                    mark = i + 1
                line[next_idx] = 0
                i = next_idx
        else:
            line[mark] = line[i]
            line[i] = 0
            # i = next_idx
            mark += 1
    else:
        if next_idx < size and (line[next_idx] == line[i]):
            if mark != size:
                line[mark] = line[i] + line[next_idx]
                line[i] = 0
                mark -= 1
            else:
                line[i] = line[i] + line[next_idx]
                mark = i - 1
            line[next_idx] = 0
            # i = next_idx
    return (i, mark, line)


def get_idx_of_next_non_zero(line, i, size, direction):
    if direction == 1:
        while i < size:
            if line[i] != 0:
                return i
            i += 1
        return (-1)

    else:
        while i > -1:
            if line[i] != 0:
                return i
            i -= 1
        return (-1)




def main():
    ######### TESTS ############
    test([4, 0, 0, 0], slide_line("L", "2 2 0 0"))
    test([0, 0, 0, 4], slide_line("R", "2 2 0 0"))

    test([4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], slide_line("L", "2 2 0 0 0 0 0 2 0 0 0 2 0 4"))
    test([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4], slide_line("R", "2 2 0 0 0 0 0 2 0 0 0 2 0 4"))

    test([0, 0, 4, 4], slide_line("R", "2 2 2 2"))
    test([4, 4, 0, 0], slide_line("L", "2 2 2 2"))

    test([0, 0, 2, 4, 4], slide_line("R", "2 2 2 2 2"))
    test([4, 4, 2, 0, 0], slide_line("L", "2 2 2 2 2"))

    test([2, 4, 8, 16], slide_line("L", "2 4 8 16"))
    test([2, 4, 8, 16], slide_line("R", "2 4 8 16"))

    test([0, 8, 8, 16], slide_line("R", "4 4 8 16"))
    test([8, 8, 16, 0], slide_line("L", "4 4 8 16"))


if __name__ == "__main__":
    main()

