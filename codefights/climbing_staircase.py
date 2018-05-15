"""
203,047
CLOSE
PREV
NEXT
Description
My solutions
Leaderboard
Comments
Readme
CODEWRITING
SCORE: 0/300

You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.

Example

For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]

There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    Guaranteed constraints:
    0 ≤ n ≤ 10.

    [input] integer k

    Guaranteed constraints:
    0 ≤ k ≤ n.

    [output] array.array.integer

    An array containing all of the possible sequences in which you could climb n steps by taking them k or fewer at a time.
"""
from collections import defaultdict, Counter
test_no = 1
def climbing_staircase(n, k):
    if n == 0:
        return [[]]
    retval = []
    stk = [(n, [])]
    while stk:
        curr, lst = stk.pop()
        i = 1
        while i < k+1:
            rem = curr - i
            if rem > 0:
                stk.append((rem, lst + [i]))
            elif rem < 0:
                break
            else:
                retval.append(lst + [i])
            i += 1
    return sorted(retval)

def test(sol, retval):
    global test_no
    fail = False
    if len(sol) != len(retval):
        fail = True
    else:
        st = {tuple(x) for x in sol}
        for elem in retval:
            if tuple(elem) not in st:
                fail = True
                break
    print("{}. ".format(test_no), end="")
    test_no += 1
    # if retval != sol:
    if fail:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))


def main():
    ######### TESTS ############
    test([[1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]], climbing_staircase(4, 2))
    test([[]], climbing_staircase(0, 0))
    test([[1]], climbing_staircase(1, 1))
    test([[1,1,1,1,1,1,1],
 [1,1,1,1,1,2],
 [1,1,1,1,2,1],
 [1,1,1,1,3],
 [1,1,1,2,1,1],
 [1,1,1,2,2],
 [1,1,1,3,1],
 [1,1,2,1,1,1],
 [1,1,2,1,2],
 [1,1,2,2,1],
 [1,1,2,3],
 [1,1,3,1,1],
 [1,1,3,2],
 [1,2,1,1,1,1],
 [1,2,1,1,2],
 [1,2,1,2,1],
 [1,2,1,3],
 [1,2,2,1,1],
 [1,2,2,2],
 [1,2,3,1],
 [1,3,1,1,1],
 [1,3,1,2],
 [1,3,2,1],
 [1,3,3],
 [2,1,1,1,1,1],
 [2,1,1,1,2],
 [2,1,1,2,1],
 [2,1,1,3],
 [2,1,2,1,1],
 [2,1,2,2],
 [2,1,3,1],
 [2,2,1,1,1],
 [2,2,1,2],
 [2,2,2,1],
 [2,2,3],
 [2,3,1,1],
 [2,3,2],
 [3,1,1,1,1],
 [3,1,1,2],
 [3,1,2,1],
 [3,1,3],
 [3,2,1,1],
 [3,2,2],
 [3,3,1]], climbing_staircase(7, 3))

if __name__ == "__main__":
    main()

