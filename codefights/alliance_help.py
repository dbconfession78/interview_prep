"""
You've just started constructing a military academy. It will take t seconds to erect the building, but given that
you're in a hurry you decide this is too long to wait.

Fortunately, your Alliance offers you help to speed up construction - this is called a boost. Each member of the
Alliance can decrease the time needed to finish the building either by 10% of the initial construction time or by 1
minute (whichever is greater). However, you can't get more than 10 boosts for a given construction project. Assuming t
hat your Alliance members act optimally, find the shortest possible time it will take to build the academy.

Note:

    If 10% of the total construction time doesn't equal an integer number of seconds, then the time bonus you get is
    rounded down (for each of the Alliance members independently).
    If time decreased using boosts becomes negative you should return 0.

Example

    For t = 1000 and allianceSize = 10, the output should be
    allianceHelp(t, allianceSize) = 0.
    If each member of the Alliance boosts the building by 10% (i.e. by 100 seconds), your new academy will be
    finished instantly.

    For t = 999 and allianceSize = 11, the output should be
    allianceHelp(t, allianceSize) = 9.
    Any 10 of your 11 allies can speed the construction up by 10% (which equals 99 seconds since 99.9 is rounded down).

    For t = 100 and allianceSize = 1, the output should be
    allianceHelp(t, allianceSize) = 40.
    Your only Alliance member will boost the construction by 1 minute (i.e. 60 seconds).

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer t

    A positive integer equal to the total construction time (in seconds).

    Guaranteed constraints:
    1 ≤ t ≤ 1000.

    [input] integer allianceSize

    A non-negative integer equal to the number of your Alliance members.

    Guaranteed constraints:
    0 ≤ allianceSize ≤ 1000.

    [output] integer

    The shortest possible time it will take to build the academy.

"""

test_no = 1
from math import *
def allianceHelp(t, allianceSize):
    boost = int(max(t * .10, 60))
    if allianceSize >= 10:
        red = boost * 10
    else:
        red = boost * allianceSize
    t -= red
    if t < 0:
        return 0
    return t

def allianceHelp(t, allianceSize):
    # if allianceSize > 9:
    perc_boost = floor(t * .10)
    if perc_boost < 60:
        perc_boost = 60
    # else:
    #     perc_boost = floor(t * .10) * allianceSize
    if allianceSize > 9:
        t -= perc_boost * 10
    else:
        t -= perc_boost * allianceSize

    # if perc_boost > 60:
    #     t -= perc_boost
    # else:
    #     if allianceSize > 9:
    #         t -= (60 * 10)
    #     else:
    #         t -= 60 * allianceSize

    if t < 0:
        return 0
    return t




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
    test(0, allianceHelp(1000, 10))
    test(9, allianceHelp(999, 11))
    test(40, allianceHelp(100, 1))
    test(0, allianceHelp(100, 10))
    test(9, allianceHelp(909, 500))

if __name__ == "__main__":
    main()

