from data_structures.linked_list import *
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def reverse_list_PRACTICE(self, head):
    def reverse_list(self, head):
        return


    def reverse_list_PASSED(self, head):
    # def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        w = head
        retlist = None
        lst = []
        while w:
            lst.append(w.val)
            w = w.next

        while lst:
            x = lst.pop()
            if retlist is None:
                retlist = ListNode(x)
                w = retlist
            else:
                w.next = ListNode(x)
                w = w.next
        return retlist


def main():
    # root = list_to_linked_list([])
    # print_linked_list(Solution().reverse_list((root)))  # []

    root = list_to_linked_list([1,2,3,4,5])
    print_linked_list(Solution().reverse_list(root))    # [5,4,3,2,1]

    root = list_to_linked_list([1, 2, 3])
    print_linked_list(Solution().reverse_list((root)))  # [3,2,1]

# LC input
# []
# [1,2,3,4,5]
# [1,2,3]

if __name__ == '__main__':
    main()