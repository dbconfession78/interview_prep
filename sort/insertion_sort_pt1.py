import sys
def main():
    length = input()
    list = [int(x) for x in input().strip().split(' ')]
    tgt = list[-1]
    i = len(list) - 1
    while i >= 0:
        if i == 0:
            list[0] = tgt
            break
        if list[i-1] <= tgt:
            list[i] = tgt
            break
        list[i] = list[i - 1]
        print_iter(list)

        i -= 1
    print_iter(list)


def print_iter(list):
    for (i, elem) in enumerate(list):
        sys.stdout.write(str(elem))
        if  i != len(list)-1:
            sys.stdout.write(' ')
        else:
            print()

if __name__ == '__main__':
    main()
