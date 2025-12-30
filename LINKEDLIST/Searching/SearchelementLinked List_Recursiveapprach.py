class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def search_element(head, target):
    if head is None:
        return False
    
    if head.val == target:
        return True
    
    return search_element(head.next, target)


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
    
    target = 3
    
    if search_element(head, target):
        print(f"Element {target} found in the linked list.")
    else:
        print(f"Element {target} not found in the linked list.")

