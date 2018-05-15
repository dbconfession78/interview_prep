
import sys
import cProfile


def main():
    # n, k = map(int, input().strip().split(' '))
    # a = list(map(int, input().strip().split(' ')))
    # answer = array_left_rotation(a, n, k);
    # print(*answer, sep=' ')

    list = [1, 2, 3, 4, 5]
    array_left_rotation(list, len(list), 4)


def array_left_rotation(a, n, k):
    k = k % n
    sublist = a[:k]
    a = a[k:] + sublist
    return a





if __name__ == '__main__':
    main()
    # cProfile.run('main()')
