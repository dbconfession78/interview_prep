# Instructions
"""
Given an integer, n how many different strings of length n can be made witht the letters 'aeiou', while abiding by the following rules:
    1. 'a' can be followed only by 'e'
    2. 'e' can be followed by 'a' or 'i'
    3. 'i' can be followd by 'a,'e,' 'o,' or 'u'
    4. 'o' can be followed by 'i' or 'u'
    5. 'u' can be followed only by 'a'

    Example 1:
    input: n=1
    output: 5
    explanation: ['a', 'e', 'i', 'o', 'u']

    Example 2:
    input: n=2
    output: 10
    explanation: ['ae', 'ea', 'ei', 'iu', 'io', 'ie', 'ia', 'ou', 'oi', 'ua']

    Example 3:
    input: n=3
    output: 19
    explanation: ['aea', 'aei', 'eae', 'eiu', 'eio', 'eie', 'eia', 'iua', 'iou', 'ioi', 'iea', 'iei', 'iae', 'oua', 'oiu', 'oio', 'oie', 'oia', 'uae']


"""

import sys
import random
class Solution:
    def magical_string(self, n):
        dct = {'a': ['e'], 'e':['i', 'a'], 'i': ['a','e','o','u'], 'o': ['i', 'u'], 'u': 'a'}
        retlst = []
        for vowel in 'aeiou':
            stk = [vowel]
            while stk:
                s = stk.pop()
                if len(s) == n:
                    retlst.append(s)
                    continue
                neighbors = dct.get(s[-1])
                for neigh in neighbors:
                    stk.append(s + neigh)
        print(len(retlst))
        return retlst

def main():
    print(Solution().magical_string(1)) # 5
    print(Solution().magical_string(2)) # 10
    print(Solution().magical_string(3)) #19


if __name__ == '__main__':
    main()
