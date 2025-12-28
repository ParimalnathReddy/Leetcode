

from symtable import Class


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def postorder_traversal(node, result):
    if node is None:
        return
    
    #First we traverse left subtree
    postorder_traversal(node.left, result)

    #Then we traverse right subtree
    postorder_traversal(node.right, result)

    #Finally we visit the root node
    result.append(node.data)


if __name__ == "__main__":
    # Representing the following tree
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    result = []
    postorder_traversal(root, result)
    for value in result:
        print(value, end=' ')

