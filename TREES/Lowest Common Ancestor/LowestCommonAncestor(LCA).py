import sys

class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # string representation
    def __repr__(self):
        return str(self.data)


# Function to find the lowest common ancestor (LCA) of two nodes in a binary tree
def LCA(root, left, right):
    # Base case: if the tree is empty, return None
    if root is None:
        # print("Base case: if the tree is empty, return None")
        return None
        
    # Compare data since left/right are new Node instances
    if root.data == left.data or root.data == right.data:
        # print("Compare data since left/right are new Node instances")
        return root
    # Recursively find the LCA in the left and right subtrees
    l_lca = LCA(root.left, left, right)
    # print("l_lca: ", l_lca)
    r_lca = LCA(root.right, left, right)
    # print("r_lca: ", r_lca)
    # If both left and right are not None, return the root
    if l_lca and r_lca:
        # print("l_lca and r_lca: ", l_lca, r_lca)
        return root
    # If only one of left or right is not None, return that node
    return l_lca if l_lca else r_lca

# Driver code
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
    
    left = Node(4)
    right = Node(6)
    
    print(LCA(root, left, right))
    