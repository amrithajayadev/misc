# https://leetcode.com/problems/binary-tree-right-side-view/

class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)


def find_height_tree(root):
    if root is None:
        return 0
    l_height = 1 + find_height_tree(root.left)
    r_height = 1 + find_height_tree(root.right)
    return max(l_height, r_height)


# print(find_height_tree(root))


def get_level_nodes(root, level, nodes, curr_level):
    if level == curr_level:
        nodes.append(root.val)
        return nodes
    curr_level += 1
    if root.left:
        get_level_nodes(root.left, level, nodes, curr_level)
    if root.right:
        get_level_nodes(root.right, level, nodes, curr_level)
    return nodes


def level_order_traversal(root):
    if not root:
        return

    h = find_height_tree(root)
    right_nodes = []
    for i in range(1, h + 1):
        nodes = []
        right_nodes.append(get_level_nodes(root, i, nodes, 1)[-1])
    return right_nodes


print(level_order_traversal(root))