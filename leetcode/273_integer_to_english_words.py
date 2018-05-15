# 273 Integer to English Words
"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        MAX = (2**31)-1 # input wont be higher than this
        retval = ''
        retlst = []
        m = 1
        zeros = 0
        dct1 = {1: '',
               2: 'Hundred',
               3: 'Thousand',
               5: 'Thousand',
               6: 'Million',
               7: 'Billion'}

        ones_dct = {1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'}

        tens_dct = {2: 'Twenty',
                    3: 'Thirty',
                    4: 'Forty',
                    5: 'Fifty',
                    6: 'Sixty',
                    7: 'Seventy',
                    8: 'Eighty',
                    9: 'Ninety'}

        while num > 0:
            if num < 10:
                # zeros += 1
                n = num
                retlst.insert(0, dct1[zeros])
                retlst.insert(0, ones_dct[n])

                break
            else:
                n = num % (10)
            num //= 10
            if n != 0:
                if zeros == 0:
                    retlst.append(ones_dct[n])
                elif zeros == 1:
                    retlst.insert(0, tens_dct[n])
                elif zeros > 1:
                    retlst.insert(0, dct1[zeros])
                    retlst.insert(0, ones_dct[n])

            zeros += 1


        # retval += ones_dct[num // (10)**zeros]

        print(dct1[dct1[zeros]])



def main():
    # print(Solution().numberToWords(300))
    # print(Solution().numberToWords(123))
    # print(Solution().numberToWords(333))
    # print(Solution().numberToWords(999))
    # print(Solution().numberToWords(1000))

    # print(Solution().numberToWords(1400))
    # print(Solution().numberToWords(1420))
    # print(Solution().numberToWords(1429))
    # print(Solution().numberToWords(9999))
    # print(Solution().numberToWords(1000000))
    print(Solution().numberToWords(1900000))


if __name__ == '__main__':
    main()