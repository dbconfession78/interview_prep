from functools import reduce


class Solution:
    # def letter_combinations_PRACTICE(self, digits):
    def letter_combinations(self, digits):
        retlst = ['']
        dct = {'0':' ',
               '1': '',
               '2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}

        if digits is None or digits == '':
            return []

        buttons = [dct[x] for x in digits]
        for button in buttons:
            letters = list(button)
            retlst_cpy = retlst
            new_retlst = []
            i = 0
            while i < len(letters):
                for s in retlst_cpy:
                    s_cpy = s + letters[i]
                    new_retlst.append(s_cpy)
                i += 1
            retlst = new_retlst
        return retlst





    def letter_combinations_PASSED(self, digits):
    # def letter_combinations(self, digits):
        """
        :finds all possible letter combinations
        that a given set of buttons could represent
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        retlist = ['']
        button_dict = {'1': '',
                       '2': 'abc',
                       '3': 'def',
                       '4': 'ghi',
                       '5': 'jkl',
                       '6': 'mno',
                       '7': 'pqrs',
                       '8': 'tuv',
                       '9': 'wxyz',
                       '0': ' '}

        for digit in digits:
            lst = [x for x in button_dict.get(digit)]
            new_retlist = []
            for char in lst:
                for string in retlist:
                    new_retlist.append(string+char)
            retlist = new_retlist
        return retlist

    def letter_combinations2(self, digits):
        """
        :finds all possible letter combinations
        that a given set of buttons could represent
        :type digits: str
        :rtype: List[str]
        """
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


print(Solution().letter_combinations(''))
print(Solution().letter_combinations('23'))
print(Solution().letter_combinations('236'))

# expected
# ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
# ['adm', 'bdm', 'cdm', 'aem', 'bem', 'cem', 'afm', 'bfm', 'cfm', 'adn', 'bdn', 'cdn', 'aen', 'ben', 'cen', 'afn', 'bfn', 'cfn', 'ado', 'bdo', 'cdo', 'aeo', 'beo', 'ceo', 'afo', 'bfo', 'cfo']

# LC input
# ""
# "23"
# "236"