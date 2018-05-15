"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```
"""

class Solution():
    def longest(self, s1, s2):
        return "".join(sorted(list(set(s1).union(set(s2)))))


def main():
    print(Solution().longest("aretheyhere", "yestheyarehere"))  # "aehrsty"


if __name__ == '__main__':
    main()