"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""
from data_structures.linked_list import *
class Solution:
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        tmp = head
        prev = None
        while tmp:
            x = tmp.val
            if tmp.val == val:
                prev.next = prev.next.next
            else:
                prev = tmp
            tmp = tmp.next
        return (head)

def main():
    print_linked_list(Solution().removeElements(list_to_linked_list([1,2,2,1]), 2))
    print_linked_list(Solution().removeElements(list_to_linked_list([1,1]), 1))


if __name__ == '__main__':
    main()