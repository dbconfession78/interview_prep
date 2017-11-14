#!/usr/bin/python3
# Given a singly linked list, determine if it is a palindrome.

class Node():
    """
    
    """
    def __init__(self, d, n):
        self.__data = d
        self.__next_node = n

    def get_data(self):
        return self.__data

    def set_data(self, d):
        self.__data = d

    def get_next(self):
        return self.__next_node

    def set_next(self, n):
        self.__next_node = n


class LinkedList():
    def __init__(self, r = None):
        self.__size = 0
        self.__root = r

    def get_size(self):
        return self.__size

    def add(self, d):
        new_node = Node(d, self.__root)
        self.root = new_node
        self.__size += 1

    def remove(self, d):
        this = self.root
        prev = None
        while(this):
            if this.get_next() == d:
                if prev == None:
                    self.root = this.get_next()
                else:
                    prev.set_next(this.get_next())
                self.size -= 1
            else:
                prev = this
                this = this.get_next()

    def print_ll(self):
        this_node = self.root
        prev_node = None
        while(this_node):
            if (this_node.get_next() == None):
                print('r: {}\n'.format(this_node.data))
            else:
                print('d: {}'.format(this_node.data))
            prev_node = this_node
            this_node = this_node.get_next()
               
    def get_data_at_index(self, index):
        walk = self.root
        i = 0
        while (walk.get_next() and index != i):
            walk = walk.get_next()
            i += 1
        return walk.get_data()

"""
    def count_nodes(ll):
        walk = ll.root
        i = 0
        while (walk):
            i += 1
            walk = walk.next_node

        return i
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        walk = head.root
        size = head.get_size()
        i = 0;
        while (walk):
            front = head.get_data_at_index(i)
            back = head.get_data_at_index(size-i-1)
            if walk.get_data() != back:
                return False
            walk = walk.get_next()
            i += 1
        return True
        
        
def main():
    """   """
    ll = LinkedList()
    ll.add('r')
    ll.add('a')
    ll.add('c')
    ll.add('e')
    ll.add('c')
    ll.add('a')
    ll.add('r')

    print(Solution().isPalindrome(ll))

if __name__ == '__main__':
    main()
        
