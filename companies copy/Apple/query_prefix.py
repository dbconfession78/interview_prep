# Instructions
"""
Implement a data structure that can add input strings as words and that can be queried by prefix for those words

e.g.
my_words.add("Hello")
my_words.add("Hellcat")
my_words.query("Hell") --> ["Hello", "Hellcat"]
"""

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        walk = self.root
        for c in word:
            if c not in walk.children:
                walk.children[c] = TrieNode()
            walk = walk.children[c]
        walk.is_end_of_word = True

    def search(self, word):
        walk = self.root
        i = 0
        retlst = []
        while i < len(word):
            if word[i] not in walk.children:
                return []
            else:
                walk = walk.children[word[i]]
                i += 1

        stk = [(walk.children, word)]
        while stk:
            top, word = stk.pop()
            for k, v in top.items():
                if v.is_end_of_word:
                    retlst.append(word + k)
                stk.append((v.children, word + k))
        return retlst


class Solution:
    def func(self):
        return

def main():
    trie = Trie()
    trie.insert('Hello')
    trie.insert('Hellcat')
    trie.insert('Misanthrope')
    trie.insert('Miss Angel')
    trie.insert('Mister')
    trie.insert('Mystery')
    trie.insert('Migrant')
    trie.insert('Military')
    trie.insert('Militant')
    trie.insert('help')
    trie.insert('helper')

    print(trie.search('he'))


    # print(trie.search('Mil'))   # ["Military", "Militant"]
    # print(trie.search('Mis'))   # ["Misanthrope", "Miss Angel", "Mister"]




if __name__ == '__main__':
    main()

