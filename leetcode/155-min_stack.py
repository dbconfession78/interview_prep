"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.size = 0
        self.min = None
        self.mins = []
        self.last_min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        self.size += 1
        if self.min is None:
            self.min = x
            self.mins.append(x)
        else:
            if self.min >= x:
                self.mins.append(x)
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stk[-1]
        self.stk = self.stk[:-1]
        self.size -= 1
        if self.min == x:
            self.mins.pop()
            if self.mins:
                self.min = self.mins[-1]
            else:
                self.min = None
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def print(self):
        print(self.stk)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    # stk = MinStack()
    # stk.push(-2)
    # stk.push(0)
    # stk.push(-3)
    #
    # print(stk.getMin())
    # stk.pop()
    # print(stk.top())
    # print(stk.getMin())

    # stk = MinStack()
    # stk.push(0)
    # stk.push(1)
    # stk.push(0)
    # print(stk.getMin())
    # stk.pop()
    # print(stk.getMin())

    # stk = MinStack()
    # stk.push(2147483646)
    # stk.push(2147483646)
    # stk.push(2147483647)
    # stk.print()
    # print(stk.top())
    # stk.pop()
    # print(stk.getMin())
    # stk.pop()
    # print(stk.getMin())
    # stk.pop()
    # stk.push(2147483647)
    # print(stk.top())
    # print(stk.getMin())
    # stk.push(-2147483648)
    # print(stk.top())
    # print(stk.getMin())
    # stk.pop()
    # print(stk.getMin())

    stk = MinStack()
    stk.push(-2)
    stk.push(-3)
    stk.push(-4)
    stk.push(0)
    stk.push(4)
    stk.push(-4)
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    print(stk.getMin())


if __name__ == '__main__':
    main()

# expected
# [null,null,null,null,-3,null,0,-2]
# [null,null,null,null,0,null,0]
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]

# LC input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]
# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
