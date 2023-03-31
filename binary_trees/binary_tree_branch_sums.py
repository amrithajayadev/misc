class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# # create a binary tree : 5, 6, 1, 2, 3,
# root = Node(5)
# root.left = Node(6)
# root.right = Node(1)
# root.left.left = Node(2)
# root.left.right = Node(3)

# create a binary tree : 5, 6, 1, 2, 3,
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)


def find_height(node):
    if node is None:
        return 0
    else:
        return max(1 + find_height(node.left), 1 + find_height(node.right))


sumlist = []


def preorder_traversal(node):
    if node is not None:
        if node.left is not None:
            node.left.value += node.value
            # sumlist.append(node.left.value)
            preorder_traversal(node.left)
        if node.right is not None:
            node.right.value += node.value
            # sumlist.append(node.right.value)
            preorder_traversal(node.right)
    else:
        return 0


preorder_traversal(root)

leaves = []


def print_leaves(root):
    if root is None:
        return
    if root.left:
        print_leaves(root.left)
    if root.right:
        print_leaves(root.right)
    if root.left is None and root.right is None:
        print(root.value)
        leaves.append(root.value)

print_leaves(root)
print(leaves)
