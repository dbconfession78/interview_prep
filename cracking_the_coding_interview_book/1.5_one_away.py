# Instructions
"""
There are three types of edits that can be performed on strings: insert a char., remove a char. or replace a char.
Given two strings, write a function to check if they are one edit (or zero edits) away

e.g.
'pale', 'ple'   -> True
'pales', 'pale' -> True
'pale', 'bale'  -> True
'pale', 'bake'  -> False

"""
test_no = 1
from collections import Counter


class Solution():
    # def one_edit_away_PRACTICE(self, s1, s2):
    def one_edit_away(self, s1, s2):
        return

    def one_edit_away_PASSED(self, s1, s2):
    # def one_edit_away(self, s1, s2):
        def check_replace(self, s1, s2):
            diffs = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if diffs == 1:
                        return False
                    diffs += 1
            return True

        def check_removal(self, s1, s2):
            for i, elem in enumerate(s1):
                test = s1[:i] + s1[i+1:]
                if test == s2:
                    return True
            return False

        l1 = len(s1)
        l2 = len(s2)
        if l1 == l2:
            return check_replace(s1, s2)
        elif l1 > l2:
            return check_removal(s1, s2)
        else:
            return check_removal(s2, s1)

    def one_edit_away_COUNTER(self, s1, s2):
    # def one_edit_away(self, s1, s2):
        if abs(len(s1) - len(s2)) > 1:
            return False
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        if len(counter1) < len(counter2):
            short = counter1
            long = counter2
        else:
            short = counter2
            long = counter1

        diff = (counter1 - counter2)
        if len(diff) > 1:
            return False

        for k, v in short.items():
            x = long.get(k)
            if x:
                if abs(x - v) > 1:
                    return False
        return True

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
    test(True, Solution().one_edit_away('pale', 'ple'))       # True
    test(True, Solution().one_edit_away('pales', 'pale'))     # True
    test(True, Solution().one_edit_away('pale', 'bale'))      # True
    test(False, Solution().one_edit_away('pale', 'bake'))      # False
    test(False, Solution().one_edit_away('pale', 'paleeeee'))  # False
    test(False, Solution().one_edit_away('pe', 'pale'))        # False
    test(True, Solution().one_edit_away('pae', 'pale'))       # True
    test(True, Solution().one_edit_away('palee', 'pale'))     # True
    test(False, Solution().one_edit_away('paleee', 'pale'))    # False


if __name__ == '__main__':
    main()