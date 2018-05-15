from sort.quick_sort import quicksort
import sys


def main():
    list = [int(x) for x in input("Enter space-separated list: ").strip().split(' ')]
    # list = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
    # list = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]

    list = [5, 4, 3, 2]
    pairs = find_pairs(list)
    for (i, elem) in enumerate(pairs):
        sys.stdout.write('{} '.format(pairs[i]))

def find_pairs(list):
    low = None
    pairs = []
    i = 0

    quicksort(list)
    while i < len(list):
        if i < len(list) - 1:
            a = list[i]
            b = list[i + 1]
            diff = abs(a - b)
            if low is None:
                low = diff
                pairs = [a, b]
            else:
                if diff < low:
                    low = diff
                    pairs = [a, b]
                elif diff == low:
                    pairs.append(a)
                    pairs.append(b)

        i += 1
    return pairs


if __name__ == '__main__':
    main()
