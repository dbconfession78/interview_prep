class Solution():
    def add_holes(self, num):
        if num is None:
            return 0
        if num < 10:
            return num
        dct = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}
        tmp = num
        retval = 0
        while tmp > 0:
            _this = tmp % 10
            tmp //= 10
            retval += dct.get(_this)
        return retval


def main():
    print(Solution().add_holes(630))
    print(Solution().add_holes(1288))


if __name__ == '__main__':
    main()

