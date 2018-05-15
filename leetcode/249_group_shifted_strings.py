# Instructions
"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
import collections


class Solution(object):
    # def groupStrings(self, strings):
    def groupStrings_PRACTICE(self, strings):
        return

    # 42ms
    # def groupStrings(self, strings):
    def groupStrings_LC(self, strings):
        map = collections.defaultdict(list)

        print(chr(ord('c') - 1))
    # normalize
        for s in strings:
            offset = ord(s[0]) - ord('a')
            key = ""
            for c in s:
                c = chr(ord(c) - offset)
                if c < 'a':
                    c = chr(ord(c) + 26)
                key += c
            map[key].append(s)
        ans = []
        for key in map:
            ans.append(sorted(map[key]))
        return ans

    # 61ms
    def groupStrings(self, strings):
    # def groupStrings_PASSED(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        retlst = []
        # alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 }
        for string in strings:
            _len = len(string)
            spans = []
            for i, char in enumerate(string):
                span = alpha[char] - alpha[string[i-1]]
                if span < 0:
                    span = (26 - alpha[string[i-1]]) + alpha[char]
                spans.append(span)
            if _len in dct:
                if tuple(spans) in dct[_len]:
                    dct[_len][tuple(spans)].append(string)
                else:
                    dct[_len][tuple(spans)] = [string]
            else:
                dct[_len] = {tuple(spans): [string]}

        for k, v in dct.items():
            for k, v in v.items():
                retlst.append(v)
        return retlst


def main():
    # output: [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
    print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

    # output: [['aa', 'bb'], ['a']]
    print(Solution().groupStrings(["aa", "bb", "a"]))

    # output: [['aa', 'bb'], ['b']]
    print(Solution().groupStrings(["aa", "bb", "b"]))

    # output: [['ab'], ['ba']]
    print(Solution().groupStrings(["ab","ba"]))

    # output: [["a","d","i","l"],["eqdf","qcpr"],["lpt","txb"],["yfglchzpledkq","zghmdiaqmfelr"],["kknecibjnq","llofdjckor"],["cpjtwqcdwbldwwrryuclcngw","huoybvhibgqibbwwdzhqhslb"],["lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil"],["iedda","zvuur"],["js","nw"],["lebzshcb","ohecvkfe"],["dgwlvcyubde","ilbqahdzgij"],["lwpphufxw","zkddvitlk"],["qzq","sbs"],["dclpiqbypjpfafukqmjnjg","yxgkdlwtkekavapflheieb"],["mkndeyrh","wuxnoibr"],["firomjjlidqpsdeqyn","oraxvssurmzybmnzhw"],["gkxpnpbfvjm","xbogegswmad"],["fpbnsbrkbcyzdmmmoisaa","rbnzendwnoklpyyyauemm"],["aiplrzejplumda","fnuqwejouqzrif"]]
    print(Solution().groupStrings(["fpbnsbrkbcyzdmmmoisaa","cpjtwqcdwbldwwrryuclcngw","a","fnuqwejouqzrif","js","qcpr","zghmdiaqmfelr","iedda","l","dgwlvcyubde","lpt","qzq","zkddvitlk","xbogegswmad","mkndeyrh","llofdjckor","lebzshcb","firomjjlidqpsdeqyn","dclpiqbypjpfafukqmjnjg","lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil","yxgkdlwtkekavapflheieb","oraxvssurmzybmnzhw","ohecvkfe","kknecibjnq","wuxnoibr","gkxpnpbfvjm","lwpphufxw","sbs","txb","ilbqahdzgij","i","zvuur","yfglchzpledkq","eqdf","nw","aiplrzejplumda","d","huoybvhibgqibbwwdzhqhslb","rbnzendwnoklpyyyauemm"]))


if __name__ == '__main__':
    main()

# LC input

# ["abc","bcd","acef","xyz","az","ba","a","z"]
# ["aa","bb","a"]
# ["aa","bb","b"]
# ["ab","ba"]
# ["fpbnsbrkbcyzdmmmoisaa","cpjtwqcdwbldwwrryuclcngw","a","fnuqwejouqzrif","js","qcpr","zghmdiaqmfelr","iedda","l","dgwlvcyubde","lpt","qzq","zkddvitlk","xbogegswmad","mkndeyrh","llofdjckor","lebzshcb","firomjjlidqpsdeqyn","dclpiqbypjpfafukqmjnjg","lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil","yxgkdlwtkekavapflheieb","oraxvssurmzybmnzhw","ohecvkfe","kknecibjnq","wuxnoibr","gkxpnpbfvjm","lwpphufxw","sbs","txb","ilbqahdzgij","i","zvuur","yfglchzpledkq","eqdf","nw","aiplrzejplumda","d","huoybvhibgqibbwwdzhqhslb","rbnzendwnoklpyyyauemm"]