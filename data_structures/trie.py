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

    def search(self, key):
        walk = self.root
        i = 0
        retlst = []
        while i < len(key):
            if key[i] not in walk.children:
                return ''
            else:
                walk = walk.children[key[i]]
                i += 1
        stk = [(walk.children, key)]
        while stk:
            top, word = stk.pop()
            for k, v in top.items():
                if v.is_end_of_word:
                    retlst.append(word + k)
                stk.append((v.children, word + k))
        return retlst


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

    print(trie.search('Mil'))
    print(trie.search('Mis'))
    print(trie.search('H'))


if __name__ == '__main__':
    main()

