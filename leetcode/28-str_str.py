class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        _len_n = len(needle)
        if _len_n == 0:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if haystack[i:i + _len_n] == needle:
                    return i
            i += 1
        return -1


def main():
    print(Solution().strStr('hello', 'll'))
    print(Solution().strStr('aaaaa', 'bba'))
    print(Solution().strStr('a', ''))


if __name__ == '__main__':
    main()


# expected
# 2
# -1
# 0

# LC input
# "hello"
# "ll"
# "aaaaa"
# "bba"
# "a"
# ""

#Instruction
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""