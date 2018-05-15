"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

"""


class Solution():
    def is_isogram(self, string):
        _set = set()
        for c in string:
            if c.lower() in _set:
                return False
            _set.add(c.lower())
        return True


def main():
    print(Solution().is_isogram("Dermatoglyphics"))     # True
    print(Solution().is_isogram("aba"))                 # False
    print(Solution().is_isogram("moOse"))               # False


if __name__ == '__main__':
    main()