#!/usr/bin/python3
from sys import argv
from os import path


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :finds the longest common prefix string amongst an array of strings.
        :type strs: List[str]
        :rtype: str
        """
#        input(strs)
        for (i, string) in enumerate(strs): # for each string
            for (j, char) in enumerate(string): # go through each char in the string
                for (k, _string) in enumerate(strs): # see if each other word starts with its incremental chars.
                    if string != _string:
                        if (_string.startswith(string)):
                            retval = string


                # log the growing string until it stops mathing
                # return that value

        return retval

def main():
    if len(argv) < 2:
        print('USAGE: ./{} "[<string1>, <string2>, ...]"'.format(path.basename(__file__)))
        return
    list = argv[1].split(", ")
    print(Solution().longestCommonPrefix(list))


if __name__ == '__main__':
    main()
