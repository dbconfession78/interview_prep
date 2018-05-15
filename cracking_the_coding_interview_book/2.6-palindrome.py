# Instructions
"""
Implement a function to check if a linked list is a palindrome
"""
from data_structures.linked_list import *


class Solution:
    # def palindrome_STACK(self, root):
    def palindrome(self, root):
        w_slow = root
        w_fast = root
        stk = []
        i = 0
        while w_fast and w_fast.next:
            stk.append(w_slow.val)
            w_slow = w_slow.next
            w_fast = w_fast.next.next
            i += 1
        if i % 2 != 0:
            w_slow = w_slow.next

        while w_slow:
            c = w_slow.val
            if stk.pop() != c:
                return False
            w_slow = w_slow.next
        return True

    def palindrome_MINE(self, root):
    # def palindrome(self, root):
        w = root
        _len = 0
        while w:
            _len += 1
            t = w
            w = w.next

        w = root

        mid = _len // 2
        i = 0
        while w and t and (i < mid):
            if w.val != t.val:
                return False
            w = w.next
            t = t.prev
            i += 1
        return True





def main():
    print(Solution().palindrome(list_to_linked_list(['r', 'a', 'c', 'e', 'c', 'a', 'r'])))
    print(Solution().palindrome(list_to_linked_list(['r', 'a', 'c', 'e', 'c', 'f', 'r'])))




if __name__ == '__main__':
    main()