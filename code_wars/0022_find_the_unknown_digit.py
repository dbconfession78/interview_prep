"""
You are helping an archaeologist decipher some runes. He knows that this
ancient society used a Base 10 system, and that
they never start a number with a leading zero. He's figured out most of the
digits as well as a few operators, but he
needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits.

- The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear.

- Each number will be in the range from-1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.

- If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -).

- All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the
expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works,
give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his
runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a
paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune
exists.

"""
from collections import Counter
class Solution():
    def solve_runes(self, runes):
        def solve(runes):
            ops_dct = {"+": add, "-": subtract, "*": mult}
            count_set = set(int(x) for x in runes if x.isnumeric())
            eq_lst, has_double_quest = convert(runes)

            for i in range(10):
                if i in count_set or (has_double_quest and i == 0):
                    continue
                expr = [x[i] if type(x) is list else x for x in eq_lst]

                if expr[expr.index("=") + 1] == "-":
                    ans = -expr.pop(expr.index("=") + 2)
                else:
                    ans = expr.pop(expr.index("=") + 1)

                expr.pop()
                y = 0
                while y < len(expr):
                    elem = expr[y]
                    if elem in ops_dct:
                        if y == 0 and elem == "-":
                            expr[y+1] *= -1
                            y += 1
                            continue
                        op = elem
                        a = expr[y-1]
                        if expr[y+1] in ops_dct:
                            if expr[y] == "-" and expr[y+1] == "-":
                                expr[y] = "+"
                                op = expr[y]
                                expr.pop(y+1)
                                b = expr[y+1]
                            else:
                                expr[y+2] *= -1
                                b = expr[y+2]
                                y += 1
                        else:
                            b = expr[y+1]
                        func = ops_dct[op]
                        res = func(a, b)
                        if res == ans:
                            return i
                    y += 1
            return -1

        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def mult(a, b):
            return a * b

        def convert(eq):
            _len = len(eq)
            is_partial = False
            retlst = []
            ops = ["-", "+", "*", "="]
            build = ""
            has_double_quest = False

            for i in range(0, _len+1):
                if i < _len:
                    if eq[i] not in ops:
                        if eq[i] == "?":
                            is_partial = True
                        build += eq[i]
                    else:
                        if eq[i] == "=":
                            if eq[i + 1:] == "??":
                                has_double_quest = True
                        if is_partial:
                            is_partial = False
                            possibles = build_possibles(build)
                            retlst.append(possibles)
                        else:
                            if build:
                                retlst.append(int(build))
                        build = ""
                        retlst.append(eq[i])
                else:
                    if is_partial:
                        return retlst + [build_possibles(build)], has_double_quest
                    else:
                        return retlst + [(int(build))], has_double_quest

        def build_possibles(unknown):
            if unknown == "?":
                return [_ for _ in range(10)]
            possibles = []
            for i in range(10):
                possibles.append(int(unknown.replace("?", str(i))))
            return possibles

        """ ENTER METHOD HERE """
        return solve(runes)


def main():
    print(Solution().solve_runes("1+1=?"))                      # 2
    print(Solution().solve_runes("123*45?=5?088"))              # 6
    print(Solution().solve_runes("-5?*-1=5?"))                  # 0
    print(Solution().solve_runes("19--45=5?"))                  # -1
    print(Solution().solve_runes("??*??=302?"))                 # 5
    print(Solution().solve_runes("?*11=??"))                    # 2
    print(Solution().solve_runes("??605*-63=-73???5"))          # 1
    print(Solution().solve_runes("-7715?5--484?00=-28?9?5"))    # 6


if __name__ == '__main__':
    main()
