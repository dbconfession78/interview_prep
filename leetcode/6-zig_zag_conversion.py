"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
from sgk_test import test
class Solution:
    # def convert_PRACTICE(self, s, numRows):
    def convert(self, s, numRows):
        return

    def convert_PASSED(self, s, numRows):
    # def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len = len(s)
        if numRows == 1 or s_len <= numRows:
            return s

        rows = [''] * numRows
        i = j = 0
        rev = False
        r_len = len(rows)

        while True:
            rows[j] += s[i]
            if j == r_len - 1:
                rev = True
            elif j == 0:
                rev = False
            if i == s_len - 1:
                break

            j = j - 1 if rev else j + 1
            i += 1

        return ''.join(rows)


def main():
    ###### TEST CASES ######
    test("PAHNAPLSIIGYIR", Solution().convert("PAYPALISHIRING", 3))
    test("ABCD", Solution().convert("ABCD", 1))
    test("A", Solution().convert("A", 2))
    test("AB", Solution().convert("AB", 2))
    test("AB", Solution().convert("AB", 3))
    test("ACB", Solution().convert("ABC", 2))

if __name__ == '__main__':
    main()
