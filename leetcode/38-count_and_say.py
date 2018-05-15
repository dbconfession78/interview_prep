class Solution:

    # def countAndSay_LC(self, n):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        arr = ['1']
        for i in range(n):
            x = arr[-1]
            before = x[0]
            s = ""
            if len(x) == 1:
                s = str(1) + x[0]
            k = 1
            for j in range(1, len(x)):
                if x[j] == before:
                    k += 1
                else:
                    s += str(k) + before
                    before = x[j]
                    k = 1

                if j == len(x) - 1:
                    s += str(k) + before
            arr.append(s)
        return arr[-2]

    def countAndSay_MINE(self, n):
    # def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {1: 1,
                2: 11,
                3: 21,
                4: 1211,
                5: 111221}
        # (6) 312211
        # (7) 13112221
        # (8) 1113213211
        if dict.get(n):
            return str(dict.get(n))
        num = '111221'
        ret = ''
        # num = dict.get(5)
        s = str(num)

        i = 5
        while i < n:
            s = self.trans(s)
            i += 1
        ret = s
        return ret

    def trans(self, s):
        i = 0
        counter = 0
        ret = ''
        while i < len(s):
            char = s[i]
            counter = 0
            while i < len(s) and s[i] == char:
                counter += 1
                i += 1
            ret += str(counter) + char
        return ret

def main():
    # print(Solution().countAndSay(1))
    # print(Solution().countAndSay(2))
    # print(Solution().countAndSay(3))
    # print(Solution().countAndSay(4))
    # print(Solution().countAndSay(5))
    #
    # print(Solution().countAndSay(6))
    # print(Solution().countAndSay(7))
    print(Solution().countAndSay(6))


if __name__ == '__main__':
    main()

# Instructions
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""