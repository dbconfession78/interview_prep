"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

from collections import Counter
class Solution(object):
    def canConstruct_PRACTICE(self, ransomNote, magazine):
    # def canConstruct(self, ransomNote, magazine):
        return
    
    def canConstruct_PASSED(self, ransomNote, magazine):
    # def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        avail = Counter(magazine)
        for char in ransomNote:
            if char not in avail or avail[char] == 0:
                return False
            else:
                avail[char] -= 1
        return True






def main():
    print(Solution().canConstruct("a", "b"))
    print(Solution().canConstruct("aa", "ab"))
    print(Solution().canConstruct("aa", "aab"))


if __name__ == '__main__':
    main()