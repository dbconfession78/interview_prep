from collections import defaultdict
class Solution(object):
    # def maxProduct_BIT(self, words):
    def maxProduct(self, words):
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            a = d.get(mask, 0)
            b = len(w)
            d[mask] = max(a, b)

            lst = []
            for x in d:
                for y in d:
                    if not x & y:
                        ret = (d[x] * d[y])
                        lst.append(ret)

        return max(lst or [0])


def main():
    print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # 16
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))  # 4
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))  # 0

# LC input
# ["abcw","baz","foo","bar","xtfn","abcdef"]
# ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# ["a", "aa", "aaa", "aaaa"]

if __name__ == '__main__':
    main()


"""
class Solution:
    def func(self):
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
