# Instructions
"""
Implement a method to peroform basic string compression using the counts of repeated chatracters.  For example, the string 'aabcccccaaa' would become 'a2b1c5a3'.  If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)"

"""

# += concating a string runs in O(n^2) time whereas str.join() runs in-place
from collections import Counter
class Solution():
    def compress_string(self, s):
        counter = Counter()
        lst = []
        for i, char in enumerate(s):
            if i > 0:
                if char != s[i-1]:
                    x = counter.pop(s[i-1])
                    lst.append(s[i-1] + str(x))
            counter[char] += 1
            if counter and i == len(s) - 1:
                x = counter.pop(char)
                lst.append(char + str(x))
        return ''.join(lst)

def main():
    print(Solution().compress_string('aabcccccaaa'))
    print(Solution().compress_string(''))
    print(Solution().compress_string('a'))
    print(Solution().compress_string('abc'))
    print(Solution().compress_string('abcabcabcabc'))
    print(Solution().compress_string('abcabcabcabc'))



if __name__ == '__main__':
    main()