def main():
    list = [9, 3, 6, 19, 5, 22, 4, 295, 28, 55]
    list = [6,
            31415926535897932384626433832795,
            1,
            3,
            10,
            3,
            5,]
    print("sorted: {}".format(selection_sort(list)))
    print()

# comparisons: 45
# swaps: 9
def selection_sort(list):
    comps = 0
    swaps = 0
    i = 0
    pos_min = 0
    print("----------------------------------------------")
    print('unsorted: {}'.format(list))
    print("----------------------------------------------")
    while i < len(list) - 1:
        j = i + 1
        pos_min = i
        while j < len(list):
            comps += 1
            if list[j] < list[pos_min]:
                pos_min = j
            j += 1
        swaps += 1
        swap(i, pos_min, list)
        i += 1



    print('comparisons: {}'.format(comps))
    print('swaps: {}'.format(swaps))
    return list


def swap(i, j, list):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list


if __name__ == '__main__':
    main()
