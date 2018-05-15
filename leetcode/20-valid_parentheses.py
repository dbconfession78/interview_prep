class Solution:
    # def isValid_PRACTICE(self, s):
    def isValid(self, s):
        return

    def isValid_PASSED(self, s):
    # def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        if s_len == 1 or s_len % 2 != 0:
            return False
        dict = {'[': ']', '(':')', '{':'}'}
        stk = []
        for char in s:
            closer = dict.get(char)
            if closer:
                stk.append(closer)
            else:
                if not stk:
                    return False
                top = stk.pop()
                if top != char:
                    return False

        if stk:
            return False
        return True


def main():
    """Test cases"""
    print(Solution().isValid('['))
    print(Solution().isValid("[[(){[]}]]"))
    print(Solution().isValid("[[(){}]}]]"))
    print(Solution().isValid("){"))
    print(Solution().isValid("(("))
    print(Solution().isValid('[[(){}]}]]'))
    print(Solution().isValid(''))


if __name__ == '__main__':
    main()

# expected
# false
# true
# false
# false
# false
# false
# true

#LC input
# "["
# "[[(){[]}]]"
# "[[(){}]}]]"
# "){"
# "(("
# "[[(){}]}]]"
# ""

# Instructions:
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""