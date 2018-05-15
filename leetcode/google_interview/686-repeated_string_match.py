class Solution:
    # def repeatedStringMatch_LC(self, A, B):
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q + i):
                return q + i
        return -1

    def repeatedStringMatch_MINE(self, A, B):
    # def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = 1
        base_A = A
        len_B = len(B)
        if B in A:
            return 1

        while len(A) <= (len_B * 2):
            count += 1
            A += base_A
            if B in A:
                return count
        return -1



def main():
    print(Solution().repeatedStringMatch('abcd', 'cdabcdab'))  # 3
    print(Solution().repeatedStringMatch('abcabcabcabc', 'abac'))  # -1
    print(Solution().repeatedStringMatch('a', 'a'))  # 1
    print(Solution().repeatedStringMatch('aa', 'a'))  # 1
    print(Solution().repeatedStringMatch('a', 'aa'))  # 2
    print(Solution().repeatedStringMatch('bb', 'bbbbbbb'))  # 4
    print(Solution().repeatedStringMatch('abababaaba', 'aabaaba'))  # 2


if __name__ == '__main__':
    main()

# expected output
# 3
# -1
# 1
# 1
# 2
# 4
# 2

#LC Input
# "abcd"
# "cdabcdab"
# "abcabcabcabc"
# "abac"
# "a"
# "a"
# "aa"
# "a"
# "a"
# "aa"
# "bb"
# "bbbbbbb"
# "abababaaba"
# "aabaaba"



# Instructions

"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000
"""