"""
Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string str

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ str.length ≤ 104.

[input] array.array.integer pairs

An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i], you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].

Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.
"""


def swapLexOrder(str, pairs):
    retval = str
    seen = set()
    stk = [str]
    while stk:
        top = stk.pop()
        for elem in pairs:
            # lst = list(top)
            a = elem[0] - 1
            b = elem[1] - 1
            new = swap(top, a, b)
            if new not in seen:
                stk.append(new)
                if new > retval:
                    retval = new
            seen.add(new)
    return retval

def swap(str, a, b):
    lst = list(str)
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp
    new = ''.join(lst)
    return new


def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0


def main():
    retval = swapLexOrder("abdc", [[1,4], [3,4]])
    test(retval, "dbca")

    retval = swapLexOrder("abcdefgh", [[1,4], [7,8]])
    test(retval, "dbcaefhg")

    retval = swapLexOrder("acxrabdz", [[1,3], [6,8], [3,8], [2,7]])
    test(retval, "zdxrabca")

    retval = swapLexOrder("lvvyfrbhgiyexoirhunnuejzhesylojwbyatfkrv", [[13,23],
 [13,28],
 [15,20],
 [24,29],
 [6,7],
 [3,4],
 [21,30],
 [2,13],
 [12,15],
 [19,23],
 [10,19],
 [13,14],
 [6,16],
 [17,25],
 [6,21],
 [17,26],
 [5,6],
 [12,24]])
    test(retval, "lyyvurrhgxyzvonohunlfejihesiebjwbyatfkrv")


if __name__ == '__main__':
    main()


