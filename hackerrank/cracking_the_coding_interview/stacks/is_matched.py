import sys
import cProfile

import sys
import cProfile


def main():
    print(is_matched("[[]"))


def is_matched(expression):
    stack = []
    dict = {"[":"]", "{":"}", "(":")"}
    i = 0
    if len(expression) == 1:
        return False
    for c in expression:
        if dict.get(c):
            stack.append(dict[c])
        else:
            if len(stack) == 0 or c != stack[len(stack) - 1]:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    return False



if __name__ == '__main__':
    main()
    # cProfile.run('main()')