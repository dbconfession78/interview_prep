#!/usr/bin/python3
import sys


class ListNode():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.id = None


    def get_id(self):
        return self.id

class LinkedList:
    def __init__(self):
        self.length = 0
        self.root = None
        self.tail = None

    def add_node_by_data_struct(self, node):
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def add_node_by_val(self, val):
        new = ListNode(val)
        if self.root is None:
            self.root = new
            self.tail = self.root
        else:
            self.tail.next = new
            self.tail = self.tail.next
        self.length += 1

    def get_length(self):
        return self.length

    def print(self):
        if self.root is None:
            print('[]')
            return
        sys.stdout.write('[')
        w = self.root
        while w:
            sys.stdout.write(str(w.val))
            if w.next:
                sys.stdout.write(', ')
            else:
                sys.stdout.write(']\n')
            w = w.next

    def update(self):
        while self.tail.next:
            self.length += 1
            self.tail = self.tail.next

# class LinkedList():
#     def __init__(self, root=None):
#         self.root = root
#         self.tail  = root
#
#     def append(self, v):
#         new = ListNode(v)
#         if self.root is None:
#             self.root = new
#         else:
#             self.tail.next = new
#             self.tail.next.prev = self.tail
#             self.tail = self.tail.next
#
#     def print(self):
#         if self.root is None:
#             print('[]')
#             return
#         sys.stdout.write('[')
#         w = self.root
#         while w:
#             sys.stdout.write(str(w.val))
#             if w.next:
#                 sys.stdout.write(', ')
#             else:
#                 sys.stdout.write(']\n')
#             w = w.next


class Map():
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.next_list = None
        self.prev_list = None

    # change so FIFO (first add stays root)
    def add(self, data, id=None):
        new = ListNode(data, self.root)
        if id is None:
            new.id = self.size
        else:
            new.id = id
        self.root = new
        if self.root.next:
            self.root.next.prev = self.root
        self.size += 1


    # doesn't work yet
    def add_to_tail(self, data):
        new = ListNode(data)
        if self.root is None:
            self.root = new
        else:
            walk = self.get_node_at_index(0, True)
            new.prev = walk
            walk.next = new

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

    def update(self, index, data, from_end=None):
        walk = self.root
        i = 0
        while (walk and i != index):
            if from_end:
                walk = walk.prev
            else:
                walk = walk.next
            i += 1

        walk.data = data

    def print_ll(self, next=None, prev=None):
        walk = self.root            
        data = []
        data_string = ""
        while walk:
            if prev and walk.prev:
                if next:
                    sys.stdout.write('\n')
                print("prev.data: {}".format(walk.prev.data))
            # if not prev and next:
            #     print()
            if prev or next:
                sys.stdout.write('   this.data: ')
            if not prev and not next:
                data.append(walk.data)
            else:
                sys.stdout.write('{}'.format(walk.data))
            # if prev or next:
            #     print()
            # if not next:
            #     print()
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


def list_to_linked_list(lst, dll=False):
    if lst is None:
        return None
    root = None
    for (i, elem) in enumerate(lst):
        if root is None:
            root = ListNode(elem)
            w = root
        else:
            w.next = ListNode(elem)
            if dll:
                w.next.prev = w
            w = w.next
    return root


def print_linked_list(root):
    if root.prev is not None:
        print("<--circ-->", end="")
    if root is None:
        print('[]')
        return
    sys.stdout.write('[')
    w = root
    while w and w.val is not None:
        sys.stdout.write(str(w.val))
        if w.next:
            sys.stdout.write(', ')
        else:
            sys.stdout.write(']\n')
        w = w.next
    if w and w.val is None:
        if w.next == root:
            print("<-- circ -->")

def bt_to_circular_dll(root):
    """
    last node points to empty TreeNode so as to maintain  orientation
    i.e.
         TeeNode(None) <--> Root <--> TreeNode(x) <--> TreeNode(x) <--> ... <--> TreeNode(x) <--v
            ^                                                                                   |
            |<--------------------------------------------------------------------------------->|
    """
    def helper(root, dll, prev):
        if root is None:
            return dll

        dll = helper(root.left, dll, prev)
        dll.next = ListNode(root.val)
        prev = dll
        dll = dll.next
        dll.prev = prev
        dll = helper(root.right, dll, prev)
        return dll
    dll_root = ListNode(None)
    w = dll_root
    w = helper(root, w, None)
    w.next = dll_root
    w.next.prev = w
    return dll_root.next

def append_node_to_linked_list(root, node):
    w = root
    while w.next:
        w = w.next
    w.next = node
    return root


