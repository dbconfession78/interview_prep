from sgk_test import test
from data_structures.linked_list import *
def check_cycle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        fast = fast.next.next
        slow = slow.next
    return False


def main():
    ######### TESTS ############
    head = list_to_linked_list([1024,402,98,4,3,2,1,0])
    test(False, check_cycle(head))

    current = head
    for i in range(4):
        current = current.next
    current.next = head

    test(True, check_cycle(head))

if __name__ == "__main__":
    main()

