from collections import defaultdict, Counter
from sgk_test import test
test_no = 1

# def fib_PRACTICE(n):
def fib(n):
    a = b = 1
    i = 0
    while i < n-1:
        a, b = b, a+b
        i += 1
    return a



def fib_ITER(n):
# def fib(n):
    a = 1
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fib_RECURSE(n):
# def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_MEMO(n):
# def fib(n):
    def helper(n, memo):
        if memo[n] == -1:
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]
    memo = [0, 1] + [-1 for _ in range(2, n+1)]
    return helper(n, memo)


def main():
    ######### TESTS ############


    test(55, fib(10))
    test(354224848179261915075, fib(100))

if __name__ == "__main__":
    main()

