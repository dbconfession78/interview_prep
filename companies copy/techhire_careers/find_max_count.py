class Solution:
    def findMaxCount(self, numbers):
        _len = len(numbers)
        if _len == 1:
            return numbers[0]
        if _len == 0:
            return 0

        dct = {}
        retval = (None, 0)
        v = None
        for elem in numbers:
            v = dct.get(elem)
            if v:
                dct[elem] += 1
            else:
                dct[elem] = 1
            if retval is None:
                retval = (elem, dct.get(elem))

            else:
                ret_c = retval[1]
                dct_c = dct.get(elem)
                if ret_c < dct_c:
                    retval = (elem, dct_c)

        return retval[1]


def main():
    print(Solution().findMaxCount([5, 5, 42]))
    print(Solution().findMaxCount([4, 100, 21, 35, 35]))


if __name__ == '__main__':
    main()
