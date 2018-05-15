test_no = 1
def is_unstable_pair(filename1, filename2):
    return True if [x.lower() for x in sorted([filename1, filename2])] != sorted([filename1.lower(), filename2.lower()]) else False
    # a = [x.lower() for x in sorted([filename1, filename2])]
    # b = sorted([filename1.lower(), filename2.lower()])
    # if  a != b:
    #     return True
    # return False






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
    ######## TESTS ############
    test(True, is_unstable_pair("aa","AB"))
    test(False, is_unstable_pair("A", "z"))
    test(False, is_unstable_pair("yyyyyy", "Azzzzzzzzz"))
    test(True, is_unstable_pair("mehOu", "mehau"))
    test(True, is_unstable_pair("aaZ", "AAzz"))
    test(False, is_unstable_pair("fdsAs", "dzdw"))
    test(True, is_unstable_pair("aaad", "aaAdd"))
    test(True, is_unstable_pair("zzzzzAa123", "zzzzza"))
    test(False, is_unstable_pair("123za", "123Z"))
    test(True, is_unstable_pair("qwerTyu123", "qwertyu"))

if __name__ == "__main__":
    main()

