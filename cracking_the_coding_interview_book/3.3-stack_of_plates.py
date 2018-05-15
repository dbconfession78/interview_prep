# Instructions
"""
Imagine a (literal) stack of plates.  If the stack gets too high, it might topple.  Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.

Implement a data structure SetOfStacks that mimics this.  SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.  SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack.

Follow up
Implement a function popAt(index) which performs a pop operation on a specific sub-stack.
"""
import sys

class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SetOfStacks:
    def __init__(self, top=None):
        self.stacks = []
        self.top = None
        self.size = 0

    def push(self, val):
        new = StackNode(val)
        if self.top is None:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def pop(self, idx=0):
        if idx == 0:
            self.top = self.top.next
        elif idx < self.size:
            w = self.top
            i = 0
            while w and i < idx-1:
                i += 1
                w = w.next

            if w.next:
                w.next = w.next.next
        self.size -= 1

    def print_stack(self):
        w = self.top
        sys.stdout.write('top [')
        while w:
            sys.stdout.write(str(w.val))
            if w.next:
                sys.stdout.write(', ')
            w = w.next
        print(']')


class Solution:
    def stack_of_plates(self, lst):
       return


def main():
    stk = SetOfStacks()
    stk.push(2)
    stk.push(5)
    stk.print_stack()
    stk.pop()
    stk.push(3)
    stk.push(4)
    stk.push(5)
    stk.push(6)
    stk.print_stack()
    stk.pop(3)
    stk.print_stack()
    print(Solution().stack_of_plates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))




if __name__ == '__main__':
    main()