# SearchelementLinked List_Iterativeapproach.py
class Node:
    # constructor
    def __init__(self, data):
        # data
        self.val = data
        # pointer
        self.next = None

# Function to search for an element in the linked list
def search_element(head, target):
    # Base case: if the list is empty, return False
    if head is None:
        return False
    # Initialize a pointer to traverse the list
    curr = head
    # Traverse the list
    while curr is not None:
        # Check if the current node's value matches the target
        if curr.val == target:
            return True
        # Move to the next node
        curr = curr.next
    return False

# Function to print the linked list 
def print_list(head):
    # Initialize a pointer to traverse the list
    curr = head
    # Traverse the list
    while curr is not None:
        # Print the current node's value
        print(curr.val, end=" ")
        # Move to the next node
        curr = curr.next
    print()

# Driver code
if __name__ == "__main__":
    #creating the linked list
    head = None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print_list(head)
    # Search for an element in the linked list
    target = 3
    
    if search_element(head, target):
        print(f"Element {target} found in the linked list.")
    else:
        print(f"Element {target} not found in the linked list.")