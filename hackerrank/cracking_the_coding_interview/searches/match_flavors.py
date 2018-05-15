import sys
import cProfile


def main():
    trip = int(input().strip())
    for a0 in range(trip):
        money = int(input().strip())
        n = int(input().strip())
        flavors = list(map(int, input().strip().split(' ')))
        match_flavors(money, n, flavors)

    # t = 2
    # money = 4
    # fl = [1, 16, 5, 18, 2, 19, 7, 13, 6, 17, 11, 8, 14, 9, 20, 10, 3, 12, 4, 15]
    # fl = [1, 4, 5, 3, 2]


def match_flavors(money, n, flavors):
    did_find = False
    flavor_info = []
    i = 0
    while i < len(flavors):
        flavor_info.append({'id':i+1, 'cost':flavors[i]})
        i += 1

    flavors = sorted(flavor_info, key=lambda k: k['cost'])
    fl_len = len(flavors)
    while flavors[fl_len // 2].get('cost') >= money:
        flavors = flavors[:len(flavors) // 2]
        fl_len = len(flavors)

    i = 0
    j = 0
    id2 = None
    while i < fl_len:
        cost = flavors[i].get('cost')
        id1 = flavors[i].get('id')
        target = money - cost
        temp = flavors
        j = 0
        tmp_len = len(temp)
        while j < tmp_len:
            if temp[tmp_len // 2].get('cost') >= target:
                temp = temp[:tmp_len // 2]
                tmp_len = len(temp)
                j += 1
            else:
                break

        for elem in temp:
            if elem.get('cost') == target and elem.get('id') != id1:
                id2 = elem.get('id')
                did_find = True
                break
        if did_find:
            retval = sorted([id1, id2])
            break
        i += 1

    if id2 is None:
        print('NOT FOUND!')
    else:
        print('{} {}'.format(retval[0]
retval[1]))


if __name__ == '__main__':
    main()
    # cProfile.run('main()')

