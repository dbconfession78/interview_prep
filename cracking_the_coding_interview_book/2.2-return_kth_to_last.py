# Instructions
"""
Implement an algorithm to find the kth to last element of a singly linked list
"""

from data_structures.linked_list import *

class Solution:
    def return_kth_to_last(self, root, k):
        """
        returns the kth node in a sll.
        :param root: root of sll in question
        :param k: node from end to return
        :return: ListNode obj at requested point. Node's value will be 'None' if k is more than the size of the sll
        """
        w_fast = root
        w_slow = root
        for _ in range(k):
            if w_fast.next is None:
                return ListNode(None)
            w_fast = w_fast.next

        while w_fast:
            w_fast = w_fast.next
            w_slow = w_slow.next
        return w_slow



def main():
    root = list_to_linked_list([1, 10, 100, 99, 3, 4, 10, 1, 4])
    print(Solution().return_kth_to_last(root, 8).val)


if __name__ == '__main__':
    main()