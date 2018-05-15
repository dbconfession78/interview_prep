
from data_structures.linked_list import *
class Solution(object):
    # def swapPairs_PRACTICE(self, head):
    def swapPairs(self, head):
        return


    def swapPairs_PASSED(self, head):
    # def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            tmp = head.next
            head.next = None
            tmp.next = head
            head = tmp
            return head
        first = True
        w = head
        pre = None
        while w.next and w.next.next:
            if first:
                tmp = head.next
                if head.next.next is None:
                    break
                head.next = head.next.next
                tmp.next = head
                head = tmp
                pre = head.next
                w = head.next.next
                first = False
            else:
                tmp = w.next
                pre.next = tmp
                w.next = w.next.next
                tmp.next = w
                w = tmp
                pre = w.next
                w = w.next.next
        if w.next:
            tmp = w.next
            pre.next = tmp
            w.next = w.next.next
            tmp.next = w
            w = tmp
        return head


def main():
    print_linked_list(Solution().swapPairs(list_to_linked_list([1,2,3,4])))
    print_linked_list(Solution().swapPairs(list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print_linked_list(Solution().swapPairs(list_to_linked_list([1, 4, 0, 5])))
    print_linked_list(Solution().swapPairs(list_to_linked_list([1, 2, 3])))
    print_linked_list(Solution().swapPairs(list_to_linked_list([1])))
    print_linked_list(Solution().swapPairs(list_to_linked_list([1, 2])))



# LC input
# [1,2,3,4]
# [1,2,3,4,5,6,7,8,9,10]
# [1,4,0,5]
# [1,2,3]
# [1]
# [1,2]

if __name__ == '__main__':
    main()


"""
class Solution:
    def func():
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
