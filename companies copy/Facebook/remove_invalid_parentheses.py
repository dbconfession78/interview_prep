from sgk_test import test

# def remove_invalid_parentheses_PRACTICE(s):
def remove_invalid_parentheses(s):
    return


def remove_invalid_parentheses_PASSED(s):
# def remove_invalid_parentheses(s):
    open = [];
    close = []
    bal = 0
    i = 0
    lst = list(s)

    while i < len(lst) and lst[i] != "(":
        if lst[i] == ")":
            lst.pop(i)
        else:
            i += 1
    if lst == "":
        return ""

    _len = len(lst)
    while i < _len:
        c = lst[i]
        if c == "(":
            bal += 1
            open.append(i)
        if c == ")":
            bal -= 1
            close.append(i)
        i += 1

    while bal != 0:
        if bal > 0:
            lst.pop(open.pop())
            bal -= 1
        if bal < 0:
            lst.pop(close.pop())
            bal += 1

    return ''.join(lst)


def main():
    # ######### TESTS ############
    test("(()((abc)))", remove_invalid_parentheses("(()(((abc()))"))
    test("(())(((abc)))", remove_invalid_parentheses("(())(((abc()))"))
    test("", remove_invalid_parentheses(")"))
    test("", remove_invalid_parentheses(")))((("))
    test("()()(())", remove_invalid_parentheses("()()(()))"))
    test("", remove_invalid_parentheses("((((("))

if __name__ == "__main__":
    main()

