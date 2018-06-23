from sgk_test import test
from collections import Counter
class MasterMind:
    def __init__(self, m):
        self.master = m
        self.challenger = None
        return

    def score(self):
        # if self.challengers == []:
        #     print("No challenger sequences entered")
        #     return -1

        i = 0
        m_dct = Counter(self.master) # P: 2, O: 1, G: 1

        red = 0         # red: 0
        white = 0           # white: 0

        while i < len(self.challenger):
            m = self.master[i]
            ch = self.challenger[i]

            if ch == m:
                red += 1
                m_dct[ch] -= 1
            i += 1

        i = 0
        while i < len(self.challenger):
            m = self.master[i]
            ch = self.challenger[i]

            if ch in self.master and m_dct[ch] > 0:
                white += 1
                m_dct[ch] -= 1
            i += 1

        return (red, white)

def main():
    ######### TESTS ############
    mm = MasterMind("POGP") #
    mm.challenger = "OPGO" #
    test((1, 2), mm.score())

if __name__ == "__main__":
    main()

