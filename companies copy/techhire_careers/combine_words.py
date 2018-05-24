from sgk_test import test
class Solution:
    def combine_words(self, a, b):
        if (a is None and b is None) or (a == '' and b == ''):
            return ''
        if a is None or a == '':
            return b
        if b is None or b == '':
            return a

        retval = ''
        i = j = 0
        while i < len(a) and j < len(b):
            retval += (a[i] + b[j])
            i += 1
            j += 1

        while i < len(a):
            retval += a[i]
            i += 1

        while j < len(b):
            retval += b[j]
            j += 1

        return retval

def main():
    test("azbsd", Solution().combine_words('ab', 'zsd'))
    test("adbecf", Solution().combine_words('abc', 'def'))
    test("zsd", Solution().combine_words('', 'zsd'))
    test("abc", Solution().combine_words('abc', ''))
    test("", Solution().combine_words('', ''))
    test("zsd", Solution().combine_words(None, 'zsd'))
    test("abc", Solution().combine_words('abc', None))
    test("", Solution().combine_words(None, None))



if __name__ == '__main__':
    main()

#Instructions:
"""
"""