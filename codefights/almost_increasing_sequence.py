from collections import defaultdict
def almostIncreasingSequence(sequence):
    _len = len(sequence)
    if _len <= 1:
        return True
    counter = defaultdict(int)
    counter[sequence[0]] = 1
    found_count = 0
    if sequence[0] >= sequence[1]:
        found_count += 1
    i = 1

    while i < _len:
        if i == _len-1:
            if found_count > 1:
                return False
            return True

        v = sequence[i]
        if v in counter:
            if counter[v] == 2:
                return False
        counter[v] += 1
        nxt = sequence[i+1]
        if v >= nxt:
            prev = sequence[i-1]
            if found_count == 2:
                return False
            found_count += 1
            if prev > nxt:
                if i != _len-2:
                    return False
            if prev >= nxt:
                if i < _len-2:
                    skp = sequence[i+2]
                    if v >= skp:
                        return False

        i += 1
    counter[sequence[-1]] += 1
    if counter[sequence[-1]] == 3:
        return False
    return True

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
    retval = almostIncreasingSequence([1,3,2])
    test(retval, True)

    retval = almostIncreasingSequence([1,3,2,1])
    test(retval, False)

    retval = almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1])
    test(retval, False)

    retval = almostIncreasingSequence([1, 2, 3, 4, 3, 6])
    test(retval, True)

    retval = almostIncreasingSequence([1, 2, 1, 2])
    test(retval, False)

    retval = almostIncreasingSequence([3, 5, 67, 98, 3])
    test(retval, True)

    retval = almostIncreasingSequence([1, 1, 1])
    test(retval, False)


if __name__ == '__main__':
    main()