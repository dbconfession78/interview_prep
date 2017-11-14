#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = walk = None
        carry = 0
        while l1 or l2 or carry != 0:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            sum = int(v1 + v2 + carry)
            carry = 0
            if sum > 9:
                carry = sum / 10
                sum = sum % 10
            if l3 is None:
                l3 = ListNode(sum)
                walk = l3
            else:
                walk.next = ListNode(sum)
                walk = walk.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return l3


""" case 1 """
l1 = ListNode(9)
l1.next = ListNode(8)
l2 = ListNode(8)

""" case 2 """
"""
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
"""
sol = Solution().addTwoNumbers(l1, l2)
walk = sol
while walk:
    print(walk.val)
    walk = walk.next
