from collections import defaultdict


class Poly:
    def add(self, p1, p2):
        """
        adds two single-variable polynomial expressions
        :p1: first polynomial
        :p2: second polynomial
        :return: dictionary of resulting exponent/coefficient pairs)
        * exponent key value of 0 implies no variable in coeeficient
        """
        retdct = {}
        _max = max(max(p1), max(p2))

        while _max >= 0:
            c1 = p1.get(_max)
            c2 = p2.get(_max)
            if c1 and c2:
                retdct[_max] = c1 + c2
            elif c1:
                retdct[_max] = c1
            elif c2:
                retdct[_max] = c2

            _max -= 1
        return retdct

    def sub(self, p1, p2):
        """
        subtracts one single-variable polynomial expression from another
        :p1: first polynomial
        :p2: second polynomial
        :return: dictionary of resulting exponent/coefficient pairs)
        * exponent key value of 0 implies no variable in coeeficient
        """
        retdct = {}
        _max = max(max(p1), max(p2))

        while _max >= 0:
            c1 = p1.get(_max)
            c2 = p2.get(_max)
            if c1 and c2:
                retdct[_max] = c1 - c2
            elif c1:
                retdct[_max] = c1
            elif c2:
                retdct[_max] = c2

            _max -= 1
        return retdct

    def mul(self, p1, p2):
        """
        multiplies two one-variable polynomial expressions
        :p1: first polynomial exp/coefficient dictionary
        :p2: second polynomial exp/coefficient dictionary
        :return: product exp/coefficient dictionary
        """
        retdct = defaultdict(int)
        for k1, v1 in p1.items():
            for k2, v2 in p2.items():
                    retdct[k1 + k2] += v1 * v2
        return retdct

    def div(self, p1, p2):
        retdct = defaultdict(int)
        for k1, v1 in p1.items():
            for k2, v2 in p2.items():
                retdct[k1 - k2] += round(v1 / v2, 2)
        return retdct



def main():
    # # expected: {7: 6, 3: -1, 2: 3, 1: 7, 0: 7}
    # print(Poly().add({3: 3, 1: 5, 0: 4},
    #                  {7: 6, 3: -4, 2: 3, 1: 2, 0: 3}))
    #
    # # expected {7: 6, 3: 7, 2: 3, 1: 3, 0: 1}
    # print(Poly().sub({3: 3, 1: 5, 0: 4},
    #                  {7: 6, 3: -4, 2: 3, 1: 2, 0: 3}))
    #
    # # expected {3: -2, 2: 11, 1: 10, 0: -10}
    # print(Poly().sub({3: 1, 2: 3, 1: 5, 0: -4},
    #                  {3: 3, 2: -8, 1: -5, 0: 6}))
    #
    # # expected {5: -10})
    # print(Poly().mul({2:5},
    #                  {3:-2}))
    #
    # # expected {4: 8, 3: -14, 2: 23, 1: -30}
    # print(Poly().mul({2:2, 1:-3},
    #                  {2:4, 1: -1, 0: 10}))

    print(Poly().div({3: 3},
                     {7: 6}))

    print(Poly().div({1: 5}, {3: -4}))


    print(Poly().div({3: 3, 1: 5, 0: 4},
                     {7: 6, 3: -4, 2: 3, 1: 2, 0: 3}))


if __name__ == "__main__":
    main()