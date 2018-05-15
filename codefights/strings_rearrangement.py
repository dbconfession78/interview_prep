from collections import defaultdict, Counter
import re



# def stringsRearrangement_3(inputArray):
def stringsRearrangement(inputArray):
    def build_dct(inputArray):
        



def stringsRearrangement_2(inputArray):
# def stringsRearrangement(inputArray):
    dct = {}
    counter = Counter()
    for i, elem in enumerate(inputArray):
        counter[elem] += 1
        lst = inputArray[:i] + inputArray[i+1:]
        sims = find_similar(lst, elem)
        if not sims:
            return False
        dct[elem] = sims

    if len(counter) == 1:
        return False

    s = set(inputArray)
    for i, elem in enumerate(inputArray):
        stk = [dct[elem]]
        seen = set()
        counter = Counter(inputArray)
        while stk:
            found = 0
            opts = stk.pop()
            for opt in opts:
                if opt and counter[opt]:
                    counter[opt] -= 1
                    seen.add(opt)
                    found += 1
                    if found == len(inputArray):
                        return True
                    if len(seen) == len(inputArray):
                        return True
                    stk.append(dct[opt])
    return False

def find_similar(ia, trial):

    retlst = []
    for i, c in enumerate(trial):
        p = re.compile('{}[a-z]{}'.format(trial[:i], trial[i + 1:]))
        for elem in ia:
            m = p.match(elem)

            if m and m.group(0) != trial:
                retlst.append(elem)
    return retlst


def stringsRearrangement_1(inputArray):
# def stringsRearrangement(inputArray):
    # s = set(inputArray)
    match_count = 0
    fnd = set()
    for I, X in enumerate(inputArray):
        # SANS = set()
        # if I > 0:
        #     SANS.add(inputArray[i-1])

        s = set(inputArray) - fnd
        lst = list(s)
        for i, st in enumerate(lst):
            if not s:
                s = fnd
            match = False
            for j, char in enumerate(st):
                p = re.compile('{}[a-z]{}'.format(st[:j], st[j + 1:]))
                sans_s = set()
                sans_s.add(st)
                tmp = s-sans_s
                for perm in (tmp):
                    if p.match(perm):
                        fnd.add(st)
                        s.remove(st)
                        s.remove(perm)
                        match_count += 1
                        match = True
                        break
                # if not match:
                #     return False
                if match_count == len(inputArray):
                    return True
                if match:
                    break


    return False

def test(retval, sol):
        if retval != sol:
            print("FAIL: ")
            print(f"retval: {retval}")
            print(f"expected: {sol}")
            return -1
        print("OK")
        return 0

def main():
    # retval = stringsRearrangement(["aba", "bbb", "bab"])
    # test(retval, False)
    #
    # retval = stringsRearrangement(["ab", "bb", "aa"])
    # test(retval, True)
    #
    # retval = stringsRearrangement(["q", "q"])
    # test(retval, False)
    #
    # retval = stringsRearrangement(["zzzzab", "zzzzbb", "zzzzaa"])
    # test(retval, True)
    #
    # retval = stringsRearrangement(["ab", "ad", "ef", "eg"])
    # test(retval, False)

    retval = stringsRearrangement(["abc", "abx", "axx", "abx", "abc"])
    test(retval, True)

    retval = stringsRearrangement(["abc", "abx", "axx", "abc"])
    test(retval, False)

if __name__ == '__main__':
    main()