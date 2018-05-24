from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from sgk_test import test

# def merge_k_lists_PRACTICE(lists):
from heapq import heapify, heappop, heappush
def merge_k_lists(lists):
    return


def merge_k_lists_PASSED(lists):
# def merge_k_lists(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists)]
    heapify(heap)
    retval = []

    while heap:
        val, lst_idx, elem_idx = heappop(heap)
        retval.append(val)
        _len = len(lists[lst_idx])
        if elem_idx+1 < _len:
            next_tup = (lists[lst_idx][elem_idx+1], lst_idx, elem_idx+1)
            heappush(heap, next_tup)
    return retval

def main():
    ######### TESTS ############
    test([10,12,15,15,17,20,20,30,32], merge_k_lists([[12, 15, 20], [10, 15, 30], [17, 20, 32]]))

if __name__ == "__main__":
    main()

