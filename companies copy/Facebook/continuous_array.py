"""
Given a sequence of nonnegative integers A and an integer T, return whether there is a *continuous sequence* of A that
sums up to exactly T

Example:
[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
[1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7

Note: We are looking for an O(N) solution. There is an obvious O(N^2) solution which is a good starting point but is not the final solution we are looking for. It’s important for the code to be as efficient as possible.

Question # 2: Determine if any 3 integers in an array sum to 0.

Note: The following solutions assumes that repetitions (i.e. choosing the same array element more than once)
are *allowed*, so the array [-5,1,10] contains a zero sum (-5-5+10) and so does [0] (0+0+0).

[4, 2, -1, 1, -5, 6, -4] = True
"""
test_no = 1
def continuous_array(arr, t):
    i = 0
    _len = len(arr)
    if _len == 1:
            return True if arr[0] == t else False
    while i < _len-1:
        j = i + 1
        s = arr[i]
        while i < j:
            if s == t:
                return True
            if s < t:
                s += arr[j]
                j += 1
            elif s > t:
                s -= arr[i]
                i += 1
    return False





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
    test(True, continuous_array([23, 5, 4, 7, 2, 11], 20))
    test(True, continuous_array([1, 3, 5, 23, 2], 8))
    test(False, continuous_array([1, 3, 5, 23, 2], 7))
    test(True, continuous_array([1], 1))
    test(True, continuous_array([1, 2], 3))

if __name__ == "__main__":
    main()

