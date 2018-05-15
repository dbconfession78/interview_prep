class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node



def main():
    head = Node(5)
    head.next_node = Node(10)
    head.next_node.next_node = Node(15)
    head.next_node.next_node.next_node = Node(20)

    has_cycle(head)

def has_cycle(head):
    walk = head
    walk.has_cycle = "hi"
    print(walk.has_cycle)




if __name__ == '__main__':
    main()