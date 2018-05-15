# Instructions
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""

from bisect import bisect
class Solution(object):
    def wordBreak_PRACTICE(self, s, wordDict):
    # def wordBreak(self, s, wordDict):
        # TODO your code goes here
            return

    # def wordBreak_PASSED(self, s, wordDict):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        return self.helper2(s, wordDict, 0, {})

    def helper2(self, s, wordDict, start, memo):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]
        i = start + 1
        while i <= len(s):
            if s[start:i] in wordDict and self.helper2(s, wordDict, i, memo):
                memo[start] = True
                return True
            i += 1

        memo[start] = False
        return memo[start]





def main():
    print(Solution().wordBreak('leetcode', ["leet", "code"]))           # True
    print(Solution().wordBreak('bb', ["a", "b", "bbb", "bbbb"]))        # True
    print(Solution().wordBreak('cars', ["car", "ca", "rs"]))            # True
    print(Solution().wordBreak('dogs', ["dog", "s", "gs"]))             # True
    print(Solution().wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    # True

    print(Solution().wordBreak('aaKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
    # False





# LC input
# "leetcode"
# ["leet","code"]
# "bb"
# ["a","b","bbb","bbbb"]
# "cars"
# ["car","ca","rs"]
# "dogs"
# ["dog","s","gs"]
# "aaaaaaaa"
# ["aaaa","aaa","aa"]
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# "aaKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


if __name__ == '__main__':
    main()
