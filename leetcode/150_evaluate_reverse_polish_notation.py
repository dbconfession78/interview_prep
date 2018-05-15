# Instructions
"""
Evaluate the value of an arithmetic expression in
Reverse Polish Notation: http://en.wikipedia.org/wiki/Reverse_Polish_notation

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):
    # 84ms
    # def evalRPN_PRACTICE(self, tokens):
    def evalRPN(self, tokens):
        stk = []
        for i, c in enumerate(tokens):
            if self.is_operator(c):
                a = stk.pop()
                b = stk.pop()
                stk.append(self.calculate(c, b, a))
            else:
                stk.append(int(c))
        return stk[0]

    def calculate(self, op, a, b):
        if op == '*':
            return a * b
        elif op == '-':
            return a - b
        elif op == '+':
            return a + b
        elif op == '/':
            return int(a / b)

    def is_operator(self, c):
        return c in '*/_+-'

    def evalRPN_PASSED(self, tokens):
    # def evalRPN(self, tokens):

        """
        :type tokens: List[str]
        :rtype: int
        """
        def is_operator(s):
            return True if s in ['+', '-', '/', '*'] else False

        def is_operand(s):
            if len(s) > 1 and s.startswith('-'):
                s = s[1:]
            return True if s.isnumeric() else False

        def mult(params):
            return params[0] * params[1]

        def sub(params):
            return params[0] - params[1]

        def div(params):
            x = params[0]
            y = params[1]
            retval = int(x / y)
            return retval

        dct = {
            '*': mult,
            '+': sum,
            '-': sub,
            '/': div}

        stk = []
        for i, token in enumerate(tokens):
            if is_operand(token):
                stk.append(int(token))
            elif is_operator(token):
                f = dct.get(token)
                b = stk.pop()
                a = stk.pop()
                stk.append(f([a, b]))
            else:
                print('{} is not a valid operator or operand'.format(token))
                return False
        return stk.pop()


def main():
    # print(Solution().evalRPN(["18"]))                       # 18 -> 18
    # print(Solution().evalRPN(["2", "1", "+", "3", "*"]))    # ((2 + 1) * 3) -> 9
    # print(Solution().evalRPN(["4", "13", "5", "/", "+"]))   # (4 + (13 / 5)) -> 6
    # print(Solution().evalRPN(["3", "-4", "+"]))               # (3 + -4) -> -1

    # expected:
    # 5 + (17 + (10 * (6 / (-11 * (9 + 3))))) -> 22
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# LC input
# ["18"]
# ["2", "1", "+", "3", "*"]
# ["4", "13", "5", "/", "+"]
# ["3","-4","+"]
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


if __name__ == '__main__':
    main()
