"""
Array Quadruplet

Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
"""
test_no = 1
# def find_array_quadruplet_PRACTICE(arr, s):
def find_array_quadruplet(arr, s):
   return




def find_array_quadruplet_PASSED(arr, s):
# def find_array_quadruplet(arr, s):
    _len = len(arr)
    if _len < 4:
        return []
    arr.sort()
    i = 0
    while i < _len - 3:
        j = i + 1
        while j < _len:
            k = j + 1
            l = _len - 1
            while k < l:
                a = arr[i]; b = arr[j]; c = arr[k]; d = arr[l]
                t = a + b + c + d
                if t == s:
                    return [a, b, c, d]
                elif t < s:
                    k += 1
                else:
                    l -= 1
            j += 1
        i += 1
    return []




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
    test([], find_array_quadruplet([1], 1))
    test([0, 4, 7, 9], find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))

if __name__ == "__main__":
    main()