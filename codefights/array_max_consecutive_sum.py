def arrayMaxConsecutiveSum(inputArray, k):
    s = sum(inputArray[:k])
    retval = s
    j = 0
    i = k - 1
    while i < len(inputArray)-1:
        s += inputArray[i+1]
        s -= inputArray[j]
        retval = max(retval, s)
        i += 1
        j += 1

    return max(retval, s)

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
    retval = arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2)
    test(retval, 8)

    retval = arrayMaxConsecutiveSum([1, 3, 2, 4], 3)
    test(retval, 9)

if __name__ == '__main__':
    main()