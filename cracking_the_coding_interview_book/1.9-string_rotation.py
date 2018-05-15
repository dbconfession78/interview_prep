# Instructions
"""
Assume you have a method isSubstring that checks if one word is a substring of another.  Given two strings, s1 and s2, write code to check  if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of 'erbottlewat').
"""


class Solution:
    # def string_rotation_BOOK(self, s1, s2):
    def string_rotation(self, s1, s2):
        s1s1 = s1*2
        return True if s2 in s1s1 else False


    def string_rotation_MINE(self, s1, s2):
    # def string_rotation(self, s1, s2):
        s1_len = len(s1)
        if s1_len != len(s2):
            return False
        if (s1 == '' and s2 != '') or (s2 == '' and s1 != ''):
            return False
        save = ''

        rem_len = 0
        for i in range(s1_len):
            if s2[0] != s1[i]:
                save += s1[i]
            else:
                rem_len = s1_len - i
                if s1[i:] != s2[:rem_len]:
                    return False
                break
        return isSubstring(s2[rem_len:]
save)


def isSubstring(s1, s2):
        return True if s2 in s1 else False





def main():
    print(Solution().string_rotation('waterbottle', 'erbottlewat'))
    print(Solution().string_rotation('nebudkud', 'udkudneb'))
    print(Solution().string_rotation('', ''))
    print(Solution().string_rotation('f', ''))
    print(Solution().string_rotation('fg', 'gg'))


if __name__ == '__main__':
    main()