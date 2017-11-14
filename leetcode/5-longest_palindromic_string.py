#!/usr/bin/python3
from sys import argv

def main():
    string = argv[1]
    print("len: {}".format(len(string)))
    retval = longestPalindrome(string)
    print('longest palindrome: {}'.format(retval))

def longestPalindrome(s):
    pal = ""
    retval = ""
    for i in range(len(s)):
        j = i; k = i;
        while (j >= 0 and k < len(s) and s[j] == s[k]):
            j -= 1; k += 1
        pal = s[j+1:k]
        if (len(pal) > len(retval)):
            retval = pal

        print(i)
        j = i; k = i+1;
        while (j >= 0 and k < len(s) and s[j] == s[k]):
            j -= 1; k += 1
        pal = s[j+1:k+100]
        input("pal: {}".format(pal))
        if (len(pal) > len(retval)):
            retval = pal

       
    return retval

# a b b a
if __name__ == "__main__":
    main()
