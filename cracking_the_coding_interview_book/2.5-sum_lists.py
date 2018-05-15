# Instructions
"""
You have two numbers represe4nted by a lnked list, where each node contains a single digit.  The digits are stored in reverse order, suh that the 1's digit is at the end of the list.  Write a function that adds the two numbers and returns the sum as a linked list.

e.g.
Input:  (7 - > 1 -> 6) + (5 -> 9 -> 2).  That is, 617 + 295
Output: 2 -> 1 -> 9. That is 912

Follow up:
Suppose the digits are stored in forward order. Repeat the above problem
"""
from data_structures.linked_list import *


class Solution:
    def sum_lists_REV(self, ll_1, ll_2):
    # def sum_lists(self, ll_1, ll_2):
        w1 = ll_1
        w2 = ll_2
        ll_3 = None
        sums = []
        carries = []
        while w1 and w2:
            _sum = w1.val + w2.val
            if _sum > 9:
                carries.append(_sum // 10)
                _sum %= 10
            sums.append(_sum)
            w1 = w1.next
            w2 = w2.next

        while w1:
            sums.append(w1.val)
            w1 = w1.next
        while w2:
            sums.append(w2.val)
            w2 = w2.next

        places = len(sums) - len(carries)
        for _ in range(places):
            carries.append(0)

        while carries and sums:
            new = ListNode(carries.pop() + sums.pop())
            if ll_3 is None:
                ll_3 = new
                w3 = ll_3
            else:
                w3.next = new
                w3 = w3.next

        return ll_3

    # def sum_lists_FWD(self, ll_1, ll_2):
    def sum_lists(self, ll_1, ll_2):
        w1 = ll_1
        w2 = ll_2
        ll_3 = None
        # w_3 = None
        carry = 0

        while (w1 and w2) or carry > 0:
            v1 = 0
            v2 = 0
            if w1:
                v1 = w1.val
            if w2:
                v2 = w2.val
            _sum = v1 + v2 + carry
            carry = 0
            if _sum > 9:
                carry = _sum // 10
                _sum %= 10

            new = ListNode(_sum)
            if ll_3 is None:
                ll_3 = new
                w3 = ll_3
            else:
                w3.next = new
                w3 = w3.next
            if w1:
                w1 = w1.next
            if w2:
                w2 = w2.next

        while w1:
            w3.next = ListNode(w1.val)
            w1 = w1.next
            w3 = w3.next

        while w2:
            w3.next = ListNode(w2.val)
            w2 = w2.next
            w3 = w3.next
        return ll_3


def main():
    print_linked_list(Solution().sum_lists(list_to_linked_list([7, 1, 6]), list_to_linked_list([5, 9, 2])))
    print_linked_list(Solution().sum_lists(list_to_linked_list([7, 1, 6, 7]), list_to_linked_list([5, 9, 2])))
    print_linked_list(Solution().sum_lists(list_to_linked_list([7, 1, 6]), list_to_linked_list([5, 9, 2, 9])))
    print(617 + 9295)

    print_linked_list(Solution().sum_lists_REV(list_to_linked_list([6, 1, 7]), list_to_linked_list([2, 9, 5])))



if __name__ == '__main__':
    main()