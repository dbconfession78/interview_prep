# Instructions
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct
a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.
"""


class Solution():
    # def word_break_PRACTICE(self, s, wordDict):
    def word_break(self, s, wordDict):
        return


    # solved recursively
    def word_break_REC(self, s, wordDict):
    # def word_break(self, s, wordDict):
        """
        Constructs sentences where each word is a word present in the supplied list, wordDict
        :param s: the string to search
        :param word_dict: list of valid words to search for in 's'
        :return: list of valid sentences
        """
        def helper(s, wordDict, start, memo):
            retlst = []
            if start in memo:
                return memo[start]
            if len(s) == start:
                retlst.append("")
            end = start + 1
            while end <= len(s):
                slice = s[start:end]
                if slice in wordDict:
                    lst = helper(s, wordDict, end, memo)
                    for w in lst:
                        retlst.append(slice + ("" if w == "" else " ") + w)
                end += 1
            memo[start] = retlst
            return retlst

        return helper(s, wordDict, 0, {})


    # very close but still off
    def word_break_STK(self, s, wordDict):
    # def word_break(self, s, wordDict):
        if sum([len(x) for x in wordDict]) < len(s):
            return []
        stk = [('', s, 0)]
        retlst = []
        while stk:
            word, string, start = stk.pop()
            sentence = []
            for i, c in enumerate(s[start:]):
                word += c
                if word in wordDict and word not in sentence:
                    sentence.append(word)
                    rem = string[i+1:]
                    stk.append((word, rem, i+1))
                    word = ''
            if sentence != [] and rem == '':
                retlst.append(' '.join(sentence))
        return retlst

    # this is the version I actually did live during the phone screen
    def word_break_UBER_INTERVIEW(self, s, wordDict):
    # def wordBreak(self, s, wordDict):
        if len(wordDict) == 1:
            if s  in wordDict:
                return [s]
            return []
        combos = []
        retlist = []
        while (True):
            combo = []
            i = 0
            marker = 0

            while (i <= len(s)):
                string = s[marker:i]
                if string in wordDict:
                    if not any(string in combo[:-1] for combo in combos):
                        marker = i
                        combo.append(string)
                i += 1
            if len(combo) == 0:
                break
            combos.append(combo)
            retlist.append(' '.join(combo))
        return retlist


def main():
    print(Solution().word_break('hotelfate', ["hotel", "fate", "hot", "elf", "ate"]))
    # # {'hot elf ate', 'hotel fate'}
    #
    print(Solution().word_break('catsanddog', ["cat", "cats", "and", "sand", "dog"]))  # {'cats and dog', 'cat sand dog'}
    print(Solution().word_break('a', ["a"]))                              # ['a']
    print(Solution().word_break('abcd', ["a", "abc", "b", "cd"]))         # ['a b cd']
    print(Solution().word_break('aaaaaaa', ["aaaa", "aa"]))               # []
    print(Solution().word_break('aaaaaaa', ["aaaa", "aaa"]))              # ["aaaa aaa","aaa aaaa"]


# LC input
# "catsanddog"
# ["cat", "cats", "and", "sand", "dog"]
# "hotelfate"
# ["hotel", "fate", "hot", "elf", "ate"]
# "a"
# ["a"]
# "abcd"
# ["a","abc","b","cd"]
# "aaaaaaa"
# ["aaaa","aa"]
# "aaaaaaa"
# ["aaaa","aaa"]

if __name__ == '__main__':
    main()
