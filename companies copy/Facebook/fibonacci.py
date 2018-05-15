from collections import defaultdict, Counter
test_no = 1

# def fib_PRACTICE(n):
def fib(n):
    return


def fib_ITER(n):
# def fib(n):
    a = 1
    b = 1
    lst = []
    for i in range(n-1):
        a, b = b, a+b
        lst.append(a+b)
    # print(lst)
    return a

def memoize_WITH_FIB_MEMO(fnc, n):
# def memoize(fnc, n):
    memo = {}
    if n not in memo:
        memo[n] = fnc(n)
        return memo[n]


# def fib_RECURSE(n):
class FIB:
    def __init__(self):
        self.lst = []

    def fib(self, n):
        self.lst = []
        def helper(n):
            if n <= 1:
                return n
                # return self.lst
            # self.lst.append(n)
            return helper(n-1) + helper(n-2)
        return helper(n)
        # return n


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


    test(55, fib(10))
    test(354224848179261915075, fib(100))
    # test(6765, memoize(fib, 20))
    # test(354224848179261915075, memoize(fib, 100))
    # test(12586269025, memoize(fib, 50))

if __name__ == "__main__":
    main()

