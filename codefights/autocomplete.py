test_no = 1
from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        walk = self.root
        for c in word:
            if c not in walk.children:
                walk.children[c] = Node()
            walk = walk.children[c]
        walk.is_end_of_word = True

    def query(self, word):
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


def autocomplete(wordList, actions):
    retval = []
    trie = Trie()
    for word in wordList:
        trie.add_word(word)

    prefix = ""
    for action in actions:
        if action == "PAUSE":
            if prefix != "":
                words = trie.query(prefix)
                retval.append(sorted(words))
            else:
                return []
                # retval.append(wordList)
        elif action == "BACKSPACE":
            if len(prefix) > 0:
                prefix = prefix[:len(prefix)-1]
        else:
            prefix += action

    return retval


def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print("\nsol: {}\nret: {}\n".format(sol, retval))

# 7/7 tests passed but 2/7 hidden tests passed
def main():
    ######### TESTS ############
    test([["unacceptable", "undeniable", "under", "underestimated", "understand", "understandable", "understanding",
           "understated", "unilateral", "universal", "universe"],
          ["undeniable", "under", "underestimated", "understand", "understandable", "understanding", "understated"],
          ["understand", "understandable", "understanding", "understated"], ["understated"]],
         autocomplete(wordList=["under", "understand", "understanding", "understandable", "unacceptable", "undeniable",
                                "unilateral", "universe", "universal", "underestimated", "understated"],
                      actions=["u", "n", "PAUSE", "d", "e", "PAUSE", "r", "s", "t", "a", "PAUSE", "t", "e", "PAUSE"]))


    test([["cap","cape","cat","cats"], ["cute","cuts"]],
          autocomplete(wordList=["cats", "cat", "cap", "cape", "cute", "cuts"],
                       actions=["c", "a", "PAUSE", "BACKSPACE", "u", "t", "PAUSE"]))

    test([["smart","strong","super","sweet","sweetie"], ["sweet","sweetie"], [], ["nice"],
          ["careful","caring","chill","considerate","cool","crispy","cute"], ["careful","caring"], ["careful"],
          ["acceptable"], ["dependable","dope"]],
          autocomplete(wordList=["nice", "cool", "good", "super", "rockin", "sweet", "wicked", "dope", "mad", "great",
                                 "terrific", "excellent", "wonderful", "beautiful", "unbelievable", "unreal", "twisted",
                                 "impossible", "legendary", "mythical", "real", "pleasure", "strong", "careful",
                                 "gentle", "caring", "considerate", "sweetie", "cute", "crispy", "wise", "smart",
                                 "dependable", "reliable", "thoughtful", "passionate", "qualified", "acceptable",
                                 "worrisome", "chill", "worthy"],
                       actions=["s", "PAUSE", "w", "e", "PAUSE", "a", "PAUSE", "BACKSPACE", "BACKSPACE", "BACKSPACE",
                                 "BACKSPACE", "n", "PAUSE", "BACKSPACE", "c", "PAUSE", "a", "r", "PAUSE", "e", "PAUSE",
                                 "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE", "a", "PAUSE", "BACKSPACE", "d",
                                 "PAUSE"]))

    test([["aAB", "aAb", "aaB", "aab"],["aaB", "aab"]],
         autocomplete(wordList=["aab","aaB","aAb","aAB"],
                      actions=["a", "PAUSE", "a", "PAUSE"]))


    test([], autocomplete(wordList=["no", "actions", "empty", "output"], actions=[]))
    test([["all","of","the","words"]],
         autocomplete(wordList=["all", "of", "the", "words"], actions=["PAUSE"]))

    test([[], [], [], [], []],
         autocomplete(wordList=[], actions=["e", "m", "p", "t", "y", "PAUSE", "n", "o", "t", "h", "i", "n", "g",
                                            "PAUSE", "b", "l", "a", "n", "k", "PAUSE", "s", "p", "a", "c", "e", "PAUSE",
                                            "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE",
                                            "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE",
                                            "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE",
                                            "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE", "BACKSPACE",
                                            "BACKSPACE", "BACKSPACE", "BACKSPACE", "c", "o", "o", "l", "PAUSE"]))

    test([], autocomplete(wordList=[], actions=["h", "e", "l", "l", "o", "PAUSE"]))


if __name__ == "__main__":
    main()

