from sgk_test import test

# def remove_invalid_parentheses_PRACTICE(s):
def remove_invalid_parentheses(s):
    return


def remove_invalid_parentheses_PASSED(s):
# def remove_invalid_parentheses(s):
    lst = list(s)
    bal = 0
    open = 0
    close = 0
    if len(s) == 1:
        return ""

    i = 0
    while i < len(lst):
        if lst[i] == "(":
            break
        if lst[i] == ")":
            lst.pop(i)
        else:
            i += 1

    for i in range(len(lst)):
        if lst[i] == "(":
            bal += 1
            open += 1
        elif lst[i] == ")":
            bal -= 1
            close += 1

    if open == 0 or close == 0:
        return ""
    i = len(lst) - 1
    while i > 0:
        if bal == 0:
            break
        if bal > 0:
            if lst[i] == "(":
                lst.pop(i)
                bal -= 1
        elif bal < 0:
            if lst[i] == ")":
                lst.pop(i)
                bal += 1
        i -= 1

    s = ''.join(lst)
    return s


def main():
    ######### TESTS ############
    test("(()((abc)))", remove_invalid_parentheses("(()(((abc()))"))
    test("(())(((abc)))", remove_invalid_parentheses("(())(((abc()))"))
    test("", remove_invalid_parentheses(")"))
    test("", remove_invalid_parentheses(")))((("))
    test("()()(())", remove_invalid_parentheses("()()(()))"))

if __name__ == "__main__":
    main()

