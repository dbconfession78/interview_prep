import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        walk = head
        walk.prev = None
        ll_len = 0
        dict = {}
        while walk:
            dict[ll_len] = walk
            ll_len += 1
            if walk.next:
                walk.next.prev = walk
                walk = walk.next
            else:
                break

        target = ll_len - n
        walk = dict.get(target)
        if walk.prev is None:
            return walk.next
        walk.prev.next = walk.next
        if walk.next:
            walk.next.prev = walk.prev
        return head


    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        walk = head
        walk.prev = None
        len = 0
        i = 0
        search_from_tail = False
        while walk:
            walk.idx = i
            i += 1
            len += 1
            if walk.next:
                walk.next.prev = walk
                walk = walk.next
            else:
                break
        target = len - n
        if len == 1 and target == 0:
            head.val = None
            return None
        if target < len // 2:
            walk = head
        else:
            search_from_tail = True

        if search_from_tail:
            while walk:
                if walk.idx == target:
                    walk.prev.next = walk.next
                walk = walk.prev
        else:
            while walk:
                if walk.idx == target:
                    if walk.prev is None:
                        head =  walk.next
                        head.prev = None
                        return head
                    walk.prev.next = walk.next
                walk = walk.next
        return head


def print_ll(head):
    if head is None:
        print('[]')
        return
    walk = head
    sys.stdout.write('[')
    while walk:
        sys.stdout.write(str(walk.val))
        if walk.next:
            sys.stdout.write(', ')
        else:
            sys.stdout.write(']')
        walk = walk.next
    print()




def main():
    """Test cases"""
    # case
    head = ListNode(1)
    head = Solution().removeNthFromEnd(head, 1)
    print_ll(head)

    # case
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().removeNthFromEnd(head, 4)
    print_ll(head)

    # case
    head = ListNode(1)
    head.next = ListNode(2)
    head = Solution().removeNthFromEnd(head, 2)
    print_ll(head)

    # case
    head = ListNode(1)
    head.next = ListNode(2)
    head = Solution().removeNthFromEnd(head, 1)
    print_ll(head)


if __name__ == '__main__':
    main()

# expected
# []
# [1, 3, 4, 5]
# [2]
# [1]

#LC Input
# [1]
# 1
# [1,2,3,4,5]
# 4
# [1,2]
# 2

# Instructions:
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""