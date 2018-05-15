# Instructions
"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
"""
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-')).upper()
        _len = len(S)

        rem = _len % K
        i = 0
        lst = []
        if rem > 0:
            lst.append(S[i:rem])
            i = rem
        while i < _len:
            lst.append(S[i:i+K])
            i += K
        ret_str = '-'.join(lst)
        return ret_str


def main():
    print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(Solution().licenseKeyFormatting("5F3Z-2e-9-w-P-fdw4", 4))
    print(Solution().licenseKeyFormatting("87rh-fif-f-f-f-5jff", 3))
    print(Solution().licenseKeyFormatting("2-5g-3-J", 2))
    print(Solution().licenseKeyFormatting("2", 2))
    print(Solution().licenseKeyFormatting("----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo", 99))
    print(Solution().licenseKeyFormatting("----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo---------", 99))
    print(Solution().licenseKeyFormatting("r", 1))
    print(Solution().licenseKeyFormatting("0123456789", 10))

#expected
# "5F3Z-2E9W"
# "5-F3Z2-E9WP-FDW4"
# "8-7RH-FIF-FFF-5JF"
# "2-5G-3J"
# "2"
# "K-MHVVUPIYOBPJTHZMDHZVBWQNWFDAJFIWUQVSUFRQSTUHORFISEJIBHTNEPRLBHJFNDNWFIJCTWBSKLJKRATHQSOWBOGDNAQODJO"
# "K-MHVVUPIYOBPJTHZMDHZVBWQNWFDAJFIWUQVSUFRQSTUHORFISEJIBHTNEPRLBHJFNDNWFIJCTWBSKLJKRATHQSOWBOGDNAQODJO"
# "R"
# "0123456789"

#LC INPUT
# "5F3Z-2e-9-w"
# 4
# "5F3Z-2e-9-w-P-fdw4"
# 4
# "87rh-fif-f-f-f-5jf"
# 3
# "2-5g-3-J"
# 2
# "2"
# 2
# "----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo"
# 99
# "----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo---------"
# 99
# "r"
# 1
# "0123456789"
# 10

if __name__ == '__main__':
    main()