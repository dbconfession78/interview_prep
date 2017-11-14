#!/usr/bin/python3
import sys

def main():
#    n = 11
#    s = 'middle-Outz'
#    k = 2


#    print('A = {}  Z = {}'.format(ord('A'), ord('Z')))
#    print('a = {}  z = {}'.format(ord('a'), ord('z')))
    n = int(input().strip())
    s = input().strip()
    k = (int(input().strip())) % 26
    
    new = ""
    base = 0; top = 0;
    for c in s:
        if c.isalpha():
            trans = chr(ord(c) + k)
            base, top = [97, 122] if c.islower() else [65, 90]
            if ord(trans) > top:
                trans = chr((ord(trans) % top) + base-1)   
            new += trans
        else:
            new += c
    print(new)

if __name__ == '__main__':
    main()
