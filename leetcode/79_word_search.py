"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # del_last_coord = False
        def helper(board, i, j, idx, memo):

            c = word[idx]
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[i]) - 1 or board[i][j] != c:
                return False

            _this = board[i][j]
            x = c
            if (i, j) in memo:
                return False
            memo[(i, j)] = 1
            if idx == len(word) - 1:
                if board[i][j] == word[idx]:
                    return True
                else:
                    return False

            if idx == len(word):
                return True
            if helper(board, i, j+1, idx+1, memo):
                return True
            if helper(board, i+1, j, idx+1, memo):
                return True
            if helper(board, i, j-1, idx+1, memo):
                return True
            if helper(board, i-1, j, idx+1, memo):
                return True

            del(memo[(i, j)])
            return False

        if word == "" or board is None:
            return False
        if len(word) > len(board) * len(board[0]):
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if board[i][j] == word[0]:
                    if helper(board, i, j, 0, {}):
                        return True
        return False


def main():
    print(Solution().exist([['A','B','C','E'],
                            ['S','F','C','S'],
                            ['A','D','E','E']
                            ],"ABCCED"))                # True
    #
    print(Solution().exist([['a', 'a']
                            ], "a"))                    # True

    print(Solution().exist([['S', 'T', 'E', 'V', 'E'],
                            ['T', 'U', 'A', 'V', 'L'],
                            ['A', 'A', 'R', 'V', 'L'],
                            ['T', 'T', 'T', 'K', 'Z']
                            ], "STUART"))               # True

    print(Solution().exist([['A','B','C','E']],""))     # False
    print(Solution().exist([[]],""))                    # False
    print(Solution().exist([["a", "a"]],"aaa"))         # False
    print(Solution().exist([["A","B","C","E"],
                            ["S","F","C","S"],
                            ["A","D","E","E"]
                            ],"ABCB"))                  # False

    print(Solution().exist([["A","B","C","E"],
                            ["S","F","E","S"],
                            ["A","D","E","E"]
                            ], "ABCEFSADEESE"))         # True

# LC input
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCCED"
# [["a", "a"]]
# "a"
# [["S","T","E","V","E"],["T","U","A","V","L"],["A","A","R","V","L"],["T","T","T","K","Z"]]
# "STUART"
# [["A","B","C","E"]]
# ""
# [[]]
# ""
# [["a","a"]]
# "aaa"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"
# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "ABCEFSADEESE"

if __name__ == '__main__':
    main()