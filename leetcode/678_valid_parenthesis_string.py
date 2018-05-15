"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""
class Solution():
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            if c == "(":
                lo += 1
            else:
                lo -= 1
            if c != ")":
                hi += 1
            else:
                hi -= 1
            if hi < 0:
                break
            lo = max(lo, 0)
        return lo == 0


def main():
    print(Solution().checkValidString("()"))  # T
    print(Solution().checkValidString("(*)")) # T
    print(Solution().checkValidString("(*))"))    # T
    print(Solution().checkValidString("()()((((())()))()()"))  # F
    print(Solution().checkValidString(")("))  # F
    print(Solution().checkValidString("(((******))"))   # T
    print(Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")) # false

# LC Input
# "()"
# "(*)"
# "(*))"
# "()()((((())()))()()"
# ")("
# "(((******))"
# "(())((())()()(*)(*()(())())())()()((()())((()))(*"
if __name__ == '__main__':
    main()

