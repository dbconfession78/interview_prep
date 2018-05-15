"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters = sorted(list(set(letters)))
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = (l+r) // 2
            v = letters[m]
            if v == target:
                if m == len(letters) - 1:
                    return letters[0]
                return letters[m+1]

            if target > v:
                l = m + 1
            elif target < v:
                if m > 0 and letters[m-1] > v:
                    return letters[m+1]
                r = m - 1

        if letters[m] > target:
            return letters[m]
        if m == len(letters) - 1:
            return letters[0]
        return letters[m+1]

def main():
    letters = ["c", "f", "j"]
    target = "a"
    print(Solution().nextGreatestLetter(letters, target))
    # "c'

    letters = ["c", "f", "j"]
    target = "c"
    print(Solution().nextGreatestLetter(letters, target))
    # "f"

    letters = ["c", "f", "j"]
    target = "d"
    print(Solution().nextGreatestLetter(letters, target))
    # "f"

    letters = ["c", "f", "j"]
    target = "g"
    print(Solution().nextGreatestLetter(letters, target))
    # "j"

    letters = ["c", "f", "j"]
    target = "j"
    print(Solution().nextGreatestLetter(letters, target))
    # "c"

    letters = ["c", "f", "j"]
    target = "k"
    print(Solution().nextGreatestLetter(letters, target))
    # "c"

    letters = ["e","e","e","e","e","e","n","n","n","n"]
    target = "e"
    print(Solution().nextGreatestLetter(letters, target))
    # "n"

# LC Input
# .
# .
# .
# ["e","e","e","e","e","e","n","n","n","n"]
# "e"

if __name__ == '__main__':
    main()