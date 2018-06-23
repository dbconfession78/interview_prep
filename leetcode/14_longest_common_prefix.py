"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from sgk_test import test
class Solution():
    # def longest_common_prefix_PRACTICE(self, strs):
    def longest_common_prefix(self, strs):
        return

    def longest_common_prefix_PASSED(self, strs):
    # def longest_common_prefix(self, strs):
        common = ''
        i = 0
        if len(strs) == 0:
            return common

        short_len = min([len(s) for s in strs])
        while i < short_len:
            win = strs[0][:i+1]
            if not all([s.startswith(win) for s in strs]):
                break
            common = win
            i += 1
        return common

def main():
    test("", Solution().longest_common_prefix([]))
    test("Stu", Solution().longest_common_prefix(["StuartA", "StufartB", "StusmartC",
                                                  "StudyartD", "StudenttartE", "StupiddartF"]))
    test("", Solution().longest_common_prefix([""]))
    test("a", Solution().longest_common_prefix(["a"]))
    test("", Solution().longest_common_prefix(["",""]))
    test("c", Solution().longest_common_prefix(["c","c"]))
    test("fl", Solution().longest_common_prefix(["flower","flow", "flight"]))


if __name__ == '__main__':
    main()
