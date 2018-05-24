"""
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
"""
from sgk_test import test
# def reverse_words_PRACTICE(arr):
def reverse_words(arr):
    return

def reverse_words_PASSED(arr):
# def reverse_words(arr):
    retval = []
    word = []
    _len = len(arr)

    for i in range(_len - 1, -1, -1):
        if arr[i] == " ":
                retval += (word + [" "])
                word = []
        else:
            word.insert(0, arr[i])
    if word:
        retval += word
    return retval


def main():
    ######### TESTS ############
    test([" ", " "], reverse_words([" ", " "]))
    test(["b"," "," ","a"], reverse_words(["a"," "," ","b"]))
    test(["h","e","l","l","o"], reverse_words(["h","e","l","l","o"]))
    test(["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"], reverse_words(["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]))
    test(["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"], reverse_words(["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]))
    test(["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"], reverse_words(["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]))

if __name__ == "__main__":
    main()

