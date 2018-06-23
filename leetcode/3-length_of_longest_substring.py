#Intstructions
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from sgk_test import test
# def lengthOfLongestSubstring_PRACTICE(s):
def lengthOfLongestSubstring(s): # s:
    return

def lengthOfLongestSubstring_dict(s):
# def lengthOfLongestSubstring(s):
    start = end = 0
    dict = {}
    longest = 0
    while end < len(s):
        if dict.get(s[end]) is None:
            dict[s[end]] = 1
            end += 1
            longest = max(longest, end - start)
        else:
            dict[s[start]] = None
            start += 1
    return longest

def lengthOfLongestSubstring_lst(s):
# def lengthOfLongestSubstring(s):
    # window = set()
    window = []
    start = end  = 0
    retval = 0

    while start < len(s) and end < len(s):
    # while end < len(s):
        #    while chars are uniqe, continue expanding window by 1.
        if s[end] not in window:
            # window.add(s[end])
            window.append(s[end])
            end += 1
            retval = max(retval, end - start)
        #    if char repeats, slide window right by one (don't expand)
        else:
            window.remove(s[start])
            start += 1
    return retval


def main():
    ###### TEST ######
    test(3, lengthOfLongestSubstring("abcabcbb"))
    test(1, lengthOfLongestSubstring("bbbbb"))
    test(3, lengthOfLongestSubstring("pwwkew"))
    test(1, lengthOfLongestSubstring("c"))
    test(2, lengthOfLongestSubstring("au"))
    test(3, lengthOfLongestSubstring("dvdf"))
    test(5, lengthOfLongestSubstring("tmmzuxt"))


# LC input
# "abcabcbb"
# "bbbbb"
# "pwwkew"
# "c"
# "au"
# "dvdf"
# "tmmzuxt"

if __name__ == '__main__':
        main()
