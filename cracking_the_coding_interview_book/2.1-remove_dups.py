# Instructions
"""
Write code to remove duplicates from an unsorted linked-list
How would you solve this problem if a temporary buffer is not allowed
# if not tracking counts, use a pointer and check all subsequent nodes after each step. Much longer.
"""

from data_structures.linked_list import *
from collections import Counter
class Solution:
    def remove_dups(self, root):
        counter = Counter()
        w = root
        while w:
            x = counter.get(w.val)
            if x:
                if w.prev:
                    w.prev.next = w.next
                if w.next:
                    w.next.prev = w.prev
                else:
                    w = w.prev
                    w.next = None
            else:
                counter[w.val] += 1

            w = w.next


def main():
    lst = [1, 10, 100, 99, 3, 4, 10, 1, 4]
    root = list_to_linked_list(lst)
    print_linked_list(root)
    Solution().remove_dups(root)
    print_linked_list(root)


if __name__ == '__main__':
    main()