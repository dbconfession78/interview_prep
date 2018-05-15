from collections import defaultdict, Counter
test_no = 1
def func(people):
    births = defaultdict(int)
    deaths = defaultdict(int)
    mn = float('inf')
    mx = 0
    pop = 0
    hi = 0
    retval = 0
    for x in people:
        births[x[0]] += 1
        deaths[x[1]] += 1
        mn = min(mn, x[0])
        mx = max(mx, x[1])

    for i in range(mn, mx+1):
        if i in births:
            pop += births[i]
        if i in deaths:
            pop -= deaths[i]
        if pop > hi:
            hi = pop
            retval = i


    return retval


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
    # test(5, func([[1, 20], [1, 11], [5, 8], [5, 19], [2, 20]]))
    test(5, func([[2000, 2010], [1975, 2005], [1975, 2003], [1803, 1809], [1750, 1869], [1840, 1935], [1803, 1921], [1894, 1921]]))

if __name__ == "__main__":
    main()

