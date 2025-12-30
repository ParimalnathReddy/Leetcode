import sys

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    
def insert_at_position(head, data, position):
    if position < 1:
        return head

    if position == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    curr  = head
    for i in range(1, position - 1):
        if curr is not None:
            curr = curr.next
        else:
            return head
    
    if curr is not None:
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    #creating the linked list
    head = None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print_list(head)
    
    head = insert_at_position(head, 4, 6)
    
    print_list(head)
    