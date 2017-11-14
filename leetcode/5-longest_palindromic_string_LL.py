#!/usr/bin/python3
import sys


def longest_palindrome_ll(s):
    ll = LinkedList()
    pals = []
    for i in range(len(s)):
        ll.add(s[i])
    
    ll.print_ll()
    input()

    # TODO: find longest palindrome
            
class Node():
    def __init__(self, c, nxt, prv=None):
        self.c = c
        self.nxt = nxt
        self.prv = prv


class LinkedList():
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, c):
        new = Node(c, self.root)
        self.root = new
        if self.root.nxt:
            self.root.nxt.prv = self.root
        self.size += 1

    def get_node_at_index(self, index, from_end=None):
        """ option to start from end  """
        walk = self.root
        i = 0
        while (walk and i != index):
            if from_end:
                walk = walk.prv
            else:
                walk = walk.nxt
            i += 1

        return walk

    def print_ll(self, nxt=None, prv=None):
        walk = self.root
        while walk:
            if prv and walk.prv:
                if nxt:
                    sys.stdout.write('\n')
                print("prv.c: {}".format(walk.prv.c))
            if not prv and nxt:
                print()
            if prv or nxt:
                sys.stdout.write('   this.c: ')                
            sys.stdout.write(walk.c)
            if prv or nxt:
                print()
            if not nxt:
                print()
            if nxt and walk.nxt:
                print('      nxt.c: {}'.format(walk.nxt.c),)
            walk = walk.nxt

    def get_last(self):
        walk = self.root
        while walk.nxt:
            walk = walk.nxt
        return walk



def main():
    retval = longest_palindrome_ll("hbfdjnsmracecarfjdksl")

if __name__ == "__main__":
    main()
