class Solution():
    # 22 min
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
    print(Solution().longest_common_prefix([]))     # ""

    # expected "Stu"
    print(Solution().longest_common_prefix(["StuartA", "StufartB", "StusmartC", "StudyartD", "StudenttartE", "StupiddartF"]))

    print(Solution().longest_common_prefix([""]))       # ""
    print(Solution().longest_common_prefix(["a"]))      # "a"
    print(Solution().longest_common_prefix(["",""]))    # ""
    print(Solution().longest_common_prefix(["c","c"]))  # "c"

# expected
# ""
# "Stu"
# ""
# "a"

# LC input
# []
# ["StuartA", "StufartB", "StusmartC", "StudyartD", "StudenttartE", "StupiddartF"]
# [""]
# ["a"]
# ["",""]
# ["c","c"]


if __name__ == '__main__':
    main()
