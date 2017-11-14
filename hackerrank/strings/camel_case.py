#!/usr/bin/python3
def main():
    s = "saveChangesInTheEditor"
    print(count_words(s))


def count_words(s):
    i = 0
    words = 0
    if len(s) > 0:
        if s[0].isalpha():
            words = 1

    while i < len(s):
        if s[i].isupper():
            words += 1
        i += 1

    return words
        
    

if __name__ == '__main__':
    main()
