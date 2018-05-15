def avoidObstacles_3(inputArray):
    # def avoidObstacles(inputArray):
    inputArray.sort()
    s = set(inputArray)
    full = []
    for i in range(max(inputArray)):
        if i not in s:
            full.append("-")
        else:
            full.append("X")
    print(full)
    print("input: {}".format(inputArray))
    print("s: {}".format(s))
    for i in range(min(inputArray), max(inputArray) + 1):
        if i not in s:
            if i * 2 not in s:
                return i
    return inputArray[-1] + 1


def avoidObstacles_2(inputArray):
# def avoidObstacles(inputArray):
    full = []
    s = set(inputArray)
    for i in range(max(inputArray) + 1):
        if i not in s:
            full.append("-")
        else:
            full.append("X")
    print(full)

    empty = [i for i in range(max(inputArray)) if i not in s]
    print("empty: {}".format(empty))
    print("input: {}".format(inputArray))
    print("set: {}".format(s))

    ################################################################
    inputArray.sort()

    i = 1
    while i < len(inputArray):
        t = inputArray[i]
        p = inputArray[i - 1]
        p_plus_1 = p + 1
        if t != p_plus_1:
            x = p_plus_1
            if x * 2 not in s:
                return x
        i += 1
    return inputArray[-1] + 1

# def avoidObstacles_1(inputArray):
def avoidObstacles(inputArray):
    full = []
    s = set(inputArray)
    for i in range(max(inputArray) + 1):
        if i not in s:
            full.append("-")
        else:
            full.append("X")
    # print(full)

    empty = [i for i in range(1,max(inputArray)+1) if i not in s]
    # print("empty: {}".format(empty))
    # print("input: {}".format(inputArray))
    # print("set: {}".format(s))

    ################################################################
    inputArray.sort()

    start = 0
    for jump in range(1, max(inputArray)+1):
        if jump in s:
            continue
        good = True
        if jump in s:
            start = inputArray.index(jump)

        for elem in inputArray[start:]:
            if elem % jump == 0:
                good = False
                break
        if good:
            return jump
    return inputArray[-1]+1

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
   retval = avoidObstacles([1, 3, 6, 10, 15, 21])
   test(retval, 4)

   retval = avoidObstacles([5, 3, 6, 7, 9])
   test(retval, 4)

   retval = avoidObstacles([2,3])
   test(retval, 4)

   retval = avoidObstacles([1, 4, 10, 6, 2])
   test(retval, 7)

   retval = avoidObstacles([1, 3, 4, 6, 10, 15, 21])
   test(retval, 8)

   retval = avoidObstacles([19, 32, 11, 23])
   test(retval, 3)

if __name__ == '__main__':
    main()