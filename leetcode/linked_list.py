#!/usr/bin/python3
import sys
            
class Node():
    def __init__(self, d, next, prev=None):
        self.data = d
        self.next = next
        self.prev = prev


class LinkedList():
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, d):
        new = Node(d, self.root)
        self.root = new
        if self.root.next:
            self.root.next.prev = self.root
        self.size += 1

    def get_node_at_index(self, index, from_end=None):
        """ option to start from end  """
        walk = self.root
        i = 0
        while (walk and i != index):
            if from_end:
                walk = walk.prev
            else:
                walk = walk.next
            i += 1

        return walk

    def print_ll(self, next=None, prev=None):
        walk = self.root            
        data = []
        data_string = ""
        while walk:
            if prev and walk.prev:
                if next:
                    sys.stdout.write('\n')
                print("prev.data: {}".format(walk.prev.data))
            if not prev and next:
                print()
            if prev or next:
                sys.stdout.write('   this.data: ')
            if not prev and not next:
                data.append(walk.data)
            else:
                sys.stdout.write('{}'.format(walk.data))
            if prev or next:
                print()
            if not next:
                print()
            if next and walk.next:
                print('      next.data: {}'.format(walk.next.data),)
            walk = walk.next
        if not next and not prev:
            data_string += '['
            for (i, d) in enumerate(data):
                data_string += str(d)
                if i != len(data)-1:
                    data_string += ', '
            data_string += ']'
            print(data_string)
        
    def get_last(self):
        walk = self.root
        while walk.next:
            walk = walk.next
        return walk



def main():
    retval = longest_palindrome_ll("hbfdjnsmracecarfjdksl")

if __name__ == "__main__":
    main()
