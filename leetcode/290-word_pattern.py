# Instructions
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution:
    # def word_pattern_PRACTICE(self, pattern, str):
    def word_pattern(self, pattern, str):
        return

    def word_pattern_PASSED(self, pattern, str):
    # def word_pattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern == "":
            return False
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        char_dct = {}
        word_dct = {}
        for (i, word) in enumerate(words):
            char = pattern[i]
            x = char_dct.get(char)
            x2 = word_dct.get(word)
            if x or x2:
                if (x2 != char) or (x != word):
                    return False
            else:
                char_dct[char] = word
                word_dct[word] = char
        return True


def main():
    print(Solution().word_pattern("abba", "dog cat cat dog"))    # True
    print(Solution().word_pattern("abba", "dog cat cat fish"))   # False
    print(Solution().word_pattern("", "dog cat cat fish"))       # False
    print(Solution().word_pattern("abb", "dog cat cat dog"))     # False
    print(Solution().word_pattern("abb", ""))                    # False
    print(Solution().word_pattern("", ""))                       # False
    print(Solution().word_pattern("ab", "dog dog"))              # False
    print(Solution().word_pattern("aba", "dog cat cat"))         # False

# LC input
# "abba"
# "dog cat cat dog"
# "abba"
# "dog cat cat fish"
# ""
# "dog cat cat fish"
# "abb"
# "dog cat cat dog"
# "abb"
# ""
# ""
# ""
# "ab"
# "dog dog"
# "aba"
# "dog cat cat"


if __name__ == '__main__':
    main()


# plan -> keys:
# keys -> debug (first submit):
# debug -> accepted:
# Total
