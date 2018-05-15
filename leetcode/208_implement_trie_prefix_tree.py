# Instructions
"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        walk = self.root
        for char in word:
            walk = walk.children[char]
        walk.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        walk = self.root
        for char in word:
            walk = walk.children.get(char)
            if walk is None:
                return False
        return walk.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        walk = self.root
        for char in prefix:
            walk = walk.children.get(char)
            if walk is None:
                return False
        return True


def main():
    # p_tree = Trie()
    # print(p_tree.search('a'))         # False
    # p_tree.insert('Hello')
    # p_tree.insert('Hellcat')
    # print(p_tree.search('Hello'))     # True
    # print(p_tree.startsWith('Hell'))  # True
    # print(p_tree.startsWith('Help'))  # False

    p_tree = Trie()
    p_tree.insert('ab')
    print(p_tree.search('a'))



# LC input *** NEED TO CONFIRM THIS FORMAT. HAVENT RUN IN LC
# ["Trie","search","insert","insert","search","startswith","startswith"]
# [[],["a"],["Hellcat"],["Hello"],["Hell"],["Help"] ]

if __name__ == '__main__':
    main()
