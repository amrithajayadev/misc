preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_bin_tree(preorder, inorder):
    root = Tree(preorder[0])