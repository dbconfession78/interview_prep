#!/usr/bin/python3
def main():
    s = "saveChangesInTheEditor"
    print(count_words(s))


def count_words(s):
    if len(s) < 2:
        return len(s)

    return len(([x for x in s if x.isupper()])) + 1
    

if __name__ == '__main__':
    main()
