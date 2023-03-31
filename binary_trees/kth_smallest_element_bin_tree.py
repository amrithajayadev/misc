class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Tree(5)
root.left = Tree(3)
root.right = Tree(6)
root.left.left= Tree(2)
root.left.left.left = Tree(1)
root.left.right = Tree(4)

def inorder_treaversal(root, nodes):
    if root is None:
        return
    inorder_treaversal(root.left, nodes)
    nodes.append(root.val)
    inorder_treaversal(root.right, nodes)

def kth_smallest(root, k):
    nodes = []
    inorder_treaversal(root, nodes)
    print(nodes)
    return nodes[k-1]

print(kth_smallest(root, 3))