#!/usr/bin/python3
from itertools import combinations

def main():
    s = "pvmaigytciycvjdhovwiouxxylkxjjyzrcdrbmokyqvsradegswrezhtdyrsyhg"
    letters = set(s)
    combos = list(combinations(letters, 2))
    max = 0
    for pair in combos:
        string = ""
#        string = "".join(i for i in s if i in pair)
        for c in s:
            if c in pair:
               string += c
        ret_len = check_t(string)
        if ret_len > max:
            max = ret_len
    print('max: {}'.format(max))
#        print('{}: {}'.format(ret_len, string))
        



def check_t(t):
    complete = True
    unique = count_unique(t)
    #    if unique == 2:
    i = 0
    while i < len(t)-1:
        if t[i] == t[i+1]:
            complete = False
            break
        i += 1
    if complete:
        input('COMPLETE ----> {}'.format(t))
        return (len(t))
    return 0


def count_unique(s):
    un = []
    for c in s:
        if c not in un:
            un.append(c)

    return len(un)

def solution(s):
    pass
    

if __name__ == '__main__':
    main()
