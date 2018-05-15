import sys



def main():
    n = int(input())
    info_list = []
    for i in range(n):
        info = input().strip().split(' ')
        info_dict = {'key': int(info[0]), 'val': info[1]
'idx': i}
        info_list.append(info_dict)

    reference_sort(info_list)

# I named his sort, not sure what it's really called
def reference_sort(list):
    nums_dict = {}
    for dict in list:
        key = dict['key']
        val = dict['val']
        if key in nums_dict:
            nums_dict[key].append(val)
        else:
            nums_dict[key] = [val]
    print(nums_dict)


def reference_sort_2(info_list):
    info_list = sorted(info_list, key=lambda k: k['key'])

    for elem in info_list:
        idx = elem['idx']
        val = elem['val']
        if idx < len(info_list) / 2:
            sys.stdout.write('- ')
        else:
            sys.stdout.write('{} '.format(val))


def count_nums(list):
    counts = []
    for i in range(100):
        counts.append(list.count(i))
    return counts


if __name__ == '__main__':
    main()