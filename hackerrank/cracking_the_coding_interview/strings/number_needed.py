import sys
import cProfile
from sort.merge_sort import merge_sort


def main():
    print(number_needed("", ""))


def number_needed(s1, s2):
    i = j = count = 0
    size = len(s1)+ len(s2)
    while i < len(s1) and j < len(s2):
        j = 0
        for c in s2:
            if c in s1:
                s1 = s1.replace(c, "", 1)
                s2 = s2.replace(c, "", 1)
                count += 2
            else:
                j += 1
        i += 1
    return size - count


if __name__ == '__main__':
    main()
    # cProfile.run('main()')