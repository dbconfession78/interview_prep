# Instructions
"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""

from bisect import bisect
from collections import Counter
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        tmp = list(formula)
        name = []
        mults = []
        lst = []
        open = 0
        count = Counter()
        last = ''
        while tmp:
            if tmp[-1].islower():
                curr = ''
                while not tmp[-1].isupper():
                    name.insert(0, tmp.pop())
                name.insert(0, tmp.pop())
            else:
                curr = tmp.pop()
                if curr.isdigit():
                    while tmp[-1].isdigit():
                        curr = tmp.pop() + curr
                    mults.append(int(curr) if open == 0 or not mults else mults[-1] * int(curr))
                elif curr == ')':
                    open += 1
                    if not mults:
                        mults.append(1)
                elif curr == '(':
                    open -= 1
                    mults.pop()

            if curr.isupper() or name:
                if name:
                    curr = ''.join(name)
                    name = []
                if not count.get(curr):
                    lst.insert(bisect(lst, curr), curr)
                if open == 0:
                    if mults:
                        count[curr] += mults.pop()
                    else:
                        count[curr] += 1
                else:
                    count[curr] += mults[-1] if mults else 1
                if last.isdigit():
                    if len(mults) > 1:
                        mults.pop()
            last = curr

        retval = ''
        for elem in lst:
            val = count.get(elem)
            retval += elem
            if val > 1:
                retval += str(val)

        return retval


def main():
    print(Solution().countOfAtoms('H2O'))                   # "H2O"
    print(Solution().countOfAtoms('Mg(OH)2'))               # "H2MgO2"
    print(Solution().countOfAtoms('K4(ON(SO3)2)'))          # "K4NO7S2"
    print(Solution().countOfAtoms('K4(ON(SO3)2)2'))         # "K4N2O14S4"
    print(Solution().countOfAtoms('H2O2He3Mg4'))            # "H2He3Mg4O2"
    print(Solution().countOfAtoms('(H2O2)3'))               # "H6O6"
    print(Solution().countOfAtoms('H2O2(He3(MgX)3)2X2'))    # "H2He6Mg6O2X8"
    print(Solution().countOfAtoms('Be32'))                  # "Be32"

#LC Input
# "H2O"
# "Mg(OH)2"
# "K4(ON(SO3)2)"
# "K4(ON(SO3)2)2"
# "H2O2He3Mg4"
# "(H2O2)3"
# "H2O2(He3(MgX)3)2X2"
# "Be32"

if __name__ == '__main__':
    main()