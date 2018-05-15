# Instructions
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList_PRACTICE(self, head):
    # def copyRandomList(self, head):
        return

    # def copyRandomList_MINE(self, head):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        return






def main():
    print(Solution().copyRandomList())


if __name__ == '__main__':
    main()