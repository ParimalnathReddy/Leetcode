import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def LCA(root, left, right):
    if root is None:
        return None
        
    # Compare data since left/right are new Node instances
    if root.data == left.data or root.data == right.data:
        return root
    
    l_lca = LCA(root.left, left, right)
    r_lca = LCA(root.right, left, right)
    
    if l_lca and r_lca:
        return root
        
    return l_lca if l_lca else r_lca
        
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
    