from sgk_test import test
# def slide_line_2(d, str):
def slide_line(d, str):
    def idx_of_next_non_zero(line, i, size, d):
        if d == "L":
            while i != size and line[i] == 0:
                i += 1
            return i
        if d == "R":
            while i != -1 and line[i] == 0:
                i -= 1
            return i

    def slide_right(line, size):
        searching = 0;
        mark = size;
        i = size - 1
        while i > -1:
            if line[i] == 0:
                if searching == 0:
                    searching = 1
                    if mark == size:
                        mark = i
                i -= 1
            elif searching == 1:
                searching = 0
                if i > 0:
                    ionnz = idx_of_next_non_zero(line, i - 1, size, "R")
                    if ionnz > -1 and line[i] == line[ionnz]:
                        line[i] = line[i] + line[ionnz]
                        line[ionnz] = 0
                    line[mark] = line[i]
                    line[i] = 0
                    mark -= 1
                    i = ionnz

            else:
                if (i > 0) and (line[i] == line[i-1]):
                    line[i] = line[i] + line[i-1]
                    line[i-1] = 0
                    mark = i - 1
                    i -= 1
                elif i > 0:
                    if line[i-1] == 0:
                        ionnz = idx_of_next_non_zero(line, i-1, size, "R")
                        if line[i] == line[ionnz]:
                            line[i] = line[i] + line[ionnz]
                            line[ionnz] = 0
                            mark = i - 1
                            i -= 1
                        else:
                            i -= 1
                    else:
                        i -= 1
                else:
                    i -= 1

<<<<<<< HEAD
        if i != size and i < 0:
            i = 0
            if mark < size and mark > -1 and mark != 0:
                if line[mark] == 0:
                    line[mark] = line[i]
                    line[i] = 0

    def slide_left(line, size):
        mark = -1
        searching = 0
        i = 0
        while i < size:
            if line[i] == 0:
                if searching == 0:
                    searching = 1
                    if mark == -1:
                        mark = i
                i += 1
=======
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
>>>>>>> 0be48e26caab2bdee4e570b5a3cd4b3207a8fed5
            else:
                if searching == 1:
                    searching = 0
                    ionnz = idx_of_next_non_zero(line, i+1, size, "L")
                    if ionnz < size and line[i] == line[ionnz]:
                        line[i] = line[i] + line[ionnz]
                        line[ionnz] = 0
                    line[mark] = line[i]
                    line[i] = 0
                    mark += 1
                    i = ionnz

                else:
                    if (i < size-1) and (line[i] == line[i+1]):
                        line[i] = line[i] + line[i+1]
                        line[i+1] = 0
                        mark = i + 1
                        i += 1
                    elif i < size-1:
                        if line[i+1] == 0:
                            ionnz = idx_of_next_non_zero(line, i+1, size, "L")
                            if line[i] == line[ionnz]:
                                line[i] = line[i] + line[ionnz]
                                line[ionnz] = 0
                                mark = i + 1
                                i += 1
                            else:
                                i += 1

                        else:
                            i += 1
                    else:
                        i += 1

        if i != -1 and i > size-1:
            i = size-1
            if mark < size and mark > -1 and mark != size-1:
                if line[mark] == 0:
                    line[mark] = line[i]
                    line[i] = 0


    line = [int(x) for x in str.split(' ')]
    if d == "L":
        slide_left(line, len(line))
        return line
    if d == "R":
        slide_right(line, len(line))
        return line

def slide_line_1(d, str):
# def slide_line(d, str):
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
                    next_idx = get_idx_of_next_non_zero(line, i + 1, size, 1)
                    ret = merge(mark, i, line, next_idx, 1)
                    i = ret[0]
                    mark = ret[1]
                    line = ret[2]

                else:
                    line[mark] = line[i]
                    line[i] = 0
            else:
                if i < (size - 1):
                    next_idx = get_idx_of_next_non_zero(line, i + 1, size, 1)
                    ret = merge(mark, i, line, next_idx, 1)
                    i = ret[0]
                    mark = ret[1]
                    line = ret[2]
            i += 1

        if i >= (size - 1):
            if mark > -1 and line[mark] == 0:
                line[mark] = line[size - 1]
                line[size - 1] = 0
        return line

    def slide_right(line, size):
        searching = 0;
        mark = size;
        i = size - 1
        while i > -1:
            # for (i = ((int) size - 1); i >= 0; i--)
            if line[i] == 0:
                if searching == 0:
                    searching = 1
                    if mark == size:
                        mark = i
            elif searching == 1:
                searching = 0
                if i > 0:
                    next_idx = get_idx_of_next_non_zero(line, i - 1, size, 2)
                    ret = merge(mark, i, line, next_idx, 2)
                    i = ret[0]
                    mark = ret[1]
                    line = ret[2]
                else:
                    line[mark] = line[i]
                    line[i] = 0
            else:
                if i > 0:
                    next_idx = get_idx_of_next_non_zero(line, i - 1, size, 2)
                    ret = merge(mark, i, line, next_idx, 2)
                    i = ret[0]
                    mark = ret[1]
                    line = ret[2]
            i -= 1

        if i <= 0:
            if mark < size and line[mark] == 0:
                line[mark] = line[0]
                line[0] = 0
        return line
        # if mark != size:
        #     line[mark] = line[i + 1]; line[i + 1] = 0
        # return line

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
                    # i = next_idx
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
                i = next_idx
<<<<<<< HEAD
        return (i, mark, line)
=======
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
>>>>>>> 0be48e26caab2bdee4e570b5a3cd4b3207a8fed5

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




def main():
    ######### TESTS ############
    print("###### LEFT ######")
    test([4, 0, 0, 0], slide_line("L", "0 0 2 2"))
    test([4, 0, 0, 0], slide_line("L", "2 2 0 0"))
    test([4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], slide_line("L", "2 2 0 0 0 0 0 2 0 0 0 2 0 4"))
    test([4, 4, 0, 0], slide_line("L", "2 2 2 2"))
    test([4, 4, 2, 0, 0], slide_line("L", "2 2 2 2 2"))
    test([2, 4, 8, 16], slide_line("L", "2 4 8 16"))
    test([8, 8, 16, 0], slide_line("L", "4 4 8 16"))
    test([4, 2, 0, 0], slide_line("L", "2 0 2 2"))
    test([4, 4, 0, 0, 0, 0, 0], slide_line("L", "2 0 2 0 2 0 2"))
    print("\n###### RIGHT ######")
    test([0, 0, 0, 4], slide_line("R", "0 0 2 2"))
    test([0, 0, 0, 4], slide_line("R", "2 2 0 0"))
    test([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4], slide_line("R", "2 2 0 0 0 0 0 2 0 0 0 2 0 4"))
    test([0, 0, 4, 4], slide_line("R", "2 2 2 2"))
    test([0, 0, 2, 4, 4], slide_line("R", "2 2 2 2 2"))
    test([2, 4, 8, 16], slide_line("R", "2 4 8 16"))
    test([0, 8, 8, 16], slide_line("R", "4 4 8 16"))
    test([0, 0, 2, 4], slide_line("R", "2 0 2 2"))
    test([0, 0, 0, 0, 0, 4, 4], slide_line("R", "2 0 2 0 2 0 2"))



if __name__ == "__main__":
    main()

