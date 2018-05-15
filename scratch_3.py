test_no = 1
def func():
    print("user\fhello")
    return


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
    test(None, func())
    test(1, func())

if __name__ == "__main__":
    main()

