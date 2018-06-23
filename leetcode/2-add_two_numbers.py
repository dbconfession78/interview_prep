import sys
from sgk_test import test
# Instructions
"""
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    # def addTwoNumbers_PRACTICE(self, l1, l2):
    def addTwoNumbers(self, l1, l2):
        return

    def addTwoNumbers_PASSED(self, l1, l2):
    # def addTwoNumbers(self, l1, l2):
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
        print()
        return l3

def main():
    """Test cases"""
    test([7,0,8], Solution().addTwoNumbers(build_ll([2, 4, 3]), build_ll([5, 6, 4])))
    test([7, 9], Solution().addTwoNumbers(build_ll([9, 8]), build_ll([8])))
    test([0, 1], Solution().addTwoNumbers(build_ll([5]), build_ll([5])))


def print_ll(root):
    walk = root
    while walk:
        sys.stdout.write(f'{walk.val} ')
        walk = walk.next
    print()

def build_ll(a_list):
    root = None
    for (i, elem) in enumerate(a_list):
        new = ListNode(elem)
        if root is None:
            root = new
            walk = root
        else:
            walk.next = ListNode(elem)
            walk = walk.next
    return root

if __name__ == '__main__':
    main()