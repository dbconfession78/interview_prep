#!/usr/bin/python3
from sys import argv
import enchant
import itertools
string = 'hotelfate'

def main():
    s = "hotelfate"
    word_list = ["hotel", "fate", "hot", "elf", "ate"]
    combos = []
    while (True):
        combo = []
        i = 0
        marker = 0
        while (i <= len(s)):
            string = s[marker:i]
            if string in word_list:
                if not any(string in combo for combo in combos):
                    marker = i
                    combo.append(string)
            i += 1
        if len(combo) == 0:
            break
        combos.append(combo)
    print(combos)


if __name__ == '__main__':
    main()
