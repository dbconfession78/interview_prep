def centuryFromYear(year):
    # if year < 100:
    #     return 1
    next = False
    if year % 100 != 0:
        next = True
    retval = year // 100
    if next:
        return retval+1
    return retval

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0


def main():
    retval = centuryFromYear(75627051)
    test(retval, 756271)

    retval = centuryFromYear(3)
    test(retval, 1)

    retval = centuryFromYear(1700)
    test(retval, 17)

    retval = centuryFromYear(1701)
    test(retval, 18)

    retval = centuryFromYear(0)
    test(retval, 0)


if __name__ == '__main__':
    main()