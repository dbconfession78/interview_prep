from sgk_test import test
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def get_first(*args):
        return args[0]
    return pair(get_first)


def cdr(pair):
    def get_second(*args):
        return args[1]
    return pair(get_second)


def main():
    ######### TESTS ############
    test(3, car(cons(3, 4)))
    test(4, cdr(cons(3, 4)))


if __name__ == "__main__":
    main()
