# Instructions
"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dct1 = {}
        dct2 = {}
        for i in range(len(s)):
            x = dct1.get(s[i])
            y = dct2.get(t[i])
            dct1[s[i]] = dct1[s[i]] + 1 if x else 1
            dct2[t[i]] = dct2[t[i]] + 1 if y else 1
        return True if dct1 == dct2 else False



def main():
    print(Solution().isAnagram('', ''))                         # True
    print(Solution().isAnagram('anagram', 'nagaram'))           # True
    print(Solution().isAnagram('rat', 'car'))                   # False
    print(Solution().isAnagram('fafapalmata', 'aaatfpalfma'))   # True
    print(Solution().isAnagram('', 'abc'))                      # False


#LC input
# ""
# ""
# "anagram"
# "nagaram"
# "rat"
# "car"
# "fafapalmata"
# "aaatfpalfma"
# ""
# "abc"


if __name__ == '__main__':
    main()
