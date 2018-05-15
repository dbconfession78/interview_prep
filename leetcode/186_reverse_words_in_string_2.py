# Instructions
"""
Reverse Words in a String II
Difficulty:Medium

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""
class Solution(object):
    # def reverseWords_PRACTICE(self, str):
    def reverseWords(self, str):
        _len = len(str)
        w_len = 0
        mark = 0
        for i in range(_len):
            if str[-1] != ' ':
                str.insert(mark, str.pop())
                w_len += 1
            else:
                mark += w_len
                if i < _len - 1:
                    str.insert(i, str.pop())
                    mark += 1
                w_len = 0
        print(''.join(str))



    def reverseWords_PASSED(self, str):
    # def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        _len = len(str)
        if _len == 1:
            print(str)
            return
        retlst = []
        i = _len - 1
        end = _len
        word_count = 0

        while i >= 0:
            slice = str[i:end]
            if slice[0] == ' ':
                word_count += 1
                if retlst == []:
                    slice = slice + [' ']
                retlst += slice[1:]
                while str[i-1] == ' ':
                    i -= 1
                end = i + 1
            i -= 1
            if i == 0:
                word_count += 1
                if word_count > 1:
                    slice = str[i:end-1]
                else:
                    slice = str[i:end]
                retlst += slice

                break

        for c, char in enumerate(str):
            str[c] = retlst[c]
        print(str)
        # return ''.join(retlst)

def main():
    Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
    Solution().reverseWords(["a"])
    Solution().reverseWords(["h","i","!"])

# LC input
# ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# ["a"]
# ["h","i","!"]

if __name__ == '__main__':
    main()

