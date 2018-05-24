from sgk_test import test
def index_equals_value_search(arr):
    retval = -1
    _len = len(arr)
    l = 0
    r = _len - 1
    while l <= r:
        m = (l + r) // 2
        v = arr[m]
        if v >= m:
            r = m - 1
            if v == m:
                retval = m
        else:
            l = m + 1
    return retval


def main():
    ######### TESTS ############
    test(2, index_equals_value_search([-8, 0, 2, 5]))
    test(0, index_equals_value_search([0]))
    test(0, index_equals_value_search([0, 3]))
    test(3, index_equals_value_search([-8,0,1,3,5]))
    test(2, index_equals_value_search([-5,0,2,3,10,29]))
    test(-1, index_equals_value_search([-5,0,3,4,10,18,27]))
    test(7, index_equals_value_search([-6,-5,-4,-1,1,3,5,7]))


if __name__ == "__main__":
    main()

