import sys
import cProfile
import hashlib
from hashlib import sha3_256
from collections import Counter

def main():
    #Yes
    # m, n = map(str, '6 4'.strip().split(' '))
    # magazine = "give me one grand today night".strip().split(' ')
    # ransom = "give one grand today".strip().split(' ')

    # No
    # m, n = map(str, '6 5'.strip().split(' '))
    # magazine = "two times three is not four".strip().split(' ')
    # ransom = "two times two is four".strip().split(' ')

    # Yes
    # m, n = map(str, '15 6'.strip().split(' '))
    # magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".strip().split(' ')
    # ransom = "elo lxkvg bg mwz clm w".strip().split(' ')

    # m, n = map(str, input().strip().split(' '))
    # magazine = input().strip().split(' ')
    # ransom = input().strip().split(' ')

    magazine = "this be kinda might might is not a be test also or sometimes".split(' ')
    ransom = "this might be or might not be a test".split(' ')

    answer = ransom_note(magazine, ransom)
    if answer:
        print("Yes")
    else:
        print("No")
"""
15 6
apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg
elo lxkvg bg mwz clm w
"""
def ransom_note(magazine, ransom):
    mag_ht = {}
    for elem in magazine:
        if mag_ht.get(elem) is None:
            mag_ht[elem] = 1
        else:
            mag_ht[elem] += 1

    for elem2 in ransom:
        count = mag_ht.get(elem2)
        if count is None or count == 0:
            return False
        else:
            mag_ht[elem2] = count - 1

    return True



if __name__ == '__main__':
    main()
    # cProfile.run('main()')
