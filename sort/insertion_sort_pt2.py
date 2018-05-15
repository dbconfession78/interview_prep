import sys
comps = 0
inserts = 0
shifts = 0


class Sort():
    # global comps, inserts, shifts
    def __init__(self):
        self.shifts = 0
        self.comps = 0
        self. inserts = 0

    def insertion_sort(self, list, new_elem=None):
        size = len(list)
        i = 1

        if size < 2 or (size == 2 and self.list[0] < list[1]):
            return list

        while i < size:
            elem = list[i]
            j = i
            while j >= 0:
                self.comps += 1
                if j == 0 or elem >= list[j - 1]:
                    if list[j] != elem:
                        list[j] = elem
                        self.inserts += 1
                    break

                list[j] = list[j - 1]
                self.shifts += 1
                j -= 1
            i += 1
        return list


def main():
    #list = [int(x) for x in input('Enter space separated list:').strip().split(' ')]
    list = [3,5, 6, 3]
    print('---------------------')
    sys.stdout.write('unsorted: ')
    print_iter(list)
    print('---------------------')
    sort = Sort()
    list = sort.insertion_sort(list)
    print('---------------------')
    sys.stdout.write('sorted:   ')
    print_iter(list)
    print('---------------------')

    print(f'comparisons: {sort.comps}')
    print(f'inserts: {sort.inserts}')
    print(f'shifts: {sort.shifts}')


def print_iter(list):
    for (i, elem) in enumerate(list):
        sys.stdout.write(str(elem))
        if i != len(list) - 1:
            sys.stdout.write(' ')
        else:
            print()


if __name__ == '__main__':
    main()
