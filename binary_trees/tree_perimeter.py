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


def find_perimeter(root):
    if not root:
        return 1
    return find_perimeter(root.left) + find_perimeter(root.right)


print(find_perimeter(root)//2)