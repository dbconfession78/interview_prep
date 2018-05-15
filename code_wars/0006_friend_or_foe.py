"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.

"""

class Solution():
    def friend(self, x):
        return [f for f in x if len(f) == 4]


def main():
    print(Solution().friend(["Ryan", "Kieran", "Mark"]))  # ["Ryan", "Mark"]


if __name__ == '__main__':
    main()