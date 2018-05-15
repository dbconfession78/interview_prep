# Instructions
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
from data_structures.linked_list import *

class Solution:
    # 1hr 35 min
    # def plusOne_PRACTICE(self, head):
    def plusOne(self, head):
        return


    def plusOne_PASSED(self, head):
    # def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            head.val +=1
            if head.val == 10:
                head.val = 0
                new = ListNode(1)
                new.next = head
                head = new
            return head

        s = head
        f = head.next
        while f:
            if f.next is None:
                break
            else:
                if f.val != 9:
                    s = s.next
                else:
                    if f.next.val != 9:
                        s = f
            f = f.next

        f.val += 1
        if f.val == 10:
            f.val = 0
            s.val += 1
            if s.val == 10:
                if s == head:
                    new = ListNode(1)
                    new.next = head
                    head = new
                s.val = 0
            s = s.next
            while s != f:
                if s.val == 9:
                    s.val = 0
                s = s.next
            if s.val == 9:
                s.val = 0

        return head


def main():
    print_linked_list(Solution().plusOne(list_to_linked_list([1,2,3])))   # [1,2,4]
    print_linked_list(Solution().plusOne(list_to_linked_list([9,9,9])))   # [1,0,0,0]
    print_linked_list(Solution().plusOne(list_to_linked_list([9,8,9,9,9,9,9,6,9])))   # [9,8,9,9,9,9,9,7,0]

    print_linked_list(Solution().plusOne(list_to_linked_list([0])))   # [1]
    print_linked_list(Solution().plusOne(list_to_linked_list([8,9,9,9])))   # [9,0,0,0]


# LC Input
# [1,2,3]
# [9,9,9]
# [9,8,9,9,9,9,9,6,9]
# [0]
# [8,9,9,9]
if __name__ == '__main__':
    main()
