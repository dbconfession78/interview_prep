"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.


You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.


Given 10->12->13->34->45->NULL,
return 10->13->45->12->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

"""
from data_structures.linked_list import *

class Solution(object):
    # def oddEvenList_PRACTICE(self, head):
    def oddEvenList(self, head):
        if head.next is None:
            return head
        w1 = head
        even_head = head
        w2 = head.next
        odd_head = head.next

        while True:
            if w2.next:
                w1.next = w1.next.next
                w1 = w2.next
            if w2.next and w2.next.next:
                w2.next = w2.next.next
                w2 = w1.next
            else:
                break
        w2.next = even_head

        return odd_head


    # def oddEvenList_PASSED(self, head):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or head.next.next is None:
            return head

        w1 = head
        tail = w2 = head.next

        while w2 and w2.next:
            w1.next = w2.next
            w2.next = w2.next.next

            w1 = w1.next
            w2 = w2.next

        w1.next = tail
        return head

def main():
    # [1, 3, 5, 2, 4]
    # print_linked_list(Solution().oddEvenList(list_to_linked_list([1,2,3,4,5])))

    print_linked_list(Solution().oddEvenList(list_to_linked_list([1,2,3,4,5, 6])))

    # [30, 20, 16, 10, 1]
    print_linked_list(Solution().oddEvenList(list_to_linked_list([30,10,20,1,16])))

if __name__ == "__main__":
    main()