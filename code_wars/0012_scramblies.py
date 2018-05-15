"""
Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
"""

from collections import Counter
class Solution():
    def scramble(self, s1, s2):
        dct1 = Counter(s1)
        dct2 = Counter(s2)
        for k, v in dct2.items():
            if k in dct1:
                if dct1[k] < dct2[k]:
                    return False
            else:
                return False
        return True


def main():
    print(Solution().scramble("rkqodlw", "world"))      # True




if __name__ == '__main__':
    main()