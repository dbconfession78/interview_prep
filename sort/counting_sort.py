import sys
import cProfile

def main():
    list = [3,7,3,7,1,4,4,7,1]
    counting_sort(list)
    print(list)


def counting_sort(list, in_place=False):
    """
    :param list: the list to sort
    :param in_place: option to sort in place or return a new list
    :return: none if in-place. new sorted list if in-place
    """
    aux = [0 for x in list]
    for elem in list:
        aux[elem] += 1
    i = 0
    if in_place:
        for (x, count) in enumerate(aux):
            if count != 0:
                for _ in range(count):
                    list[i] = x
                    i += 1

    else:
        ret_list = []

        i = 0
        while i < len(list):
            for j in range(aux[i]):
                ret_list.append(i)
            i += 1

        list[:] = ret_list


if __name__ == '__main__':
    main()
    # cProfile.run('main()')
