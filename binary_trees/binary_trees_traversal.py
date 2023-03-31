class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


# create a binary tree : 5, 6, 1, 2, 3,
root = Node(5)
root.left = Node(6)
root.right = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)


# Inorder traversal : 2 6 3 5 1
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)


# pre order : 5 6 2 3 1
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


# post order: 2 3 6 1 5
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")


print("---In order traversal---")
inorder_traversal(root)
print("\n---Pre order traversal---")
preorder_traversal(root)
print("\n---Post order traversal---")
postorder_traversal(root)


def find_height(node):
    if node is None:
        return 0
    else:
        return max(1 + find_height(node.left), 1 + find_height(node.right))


def print_level(node, h):
    if node is None:
        return
    if h == 1:
        print(node.value, end=" ")
    else:
        print_level(node.left, h - 1)
        print_level(node.right, h - 1)


def level_order_traversal(node):
    h = find_height(node)
    for i in range(1, h + 1):
        print_level(node, i)


print("\nLevel order traversal")
level_order_traversal(root)
