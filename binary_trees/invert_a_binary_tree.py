import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(array):
    def create_node(l, r):
        if l > r:
            return
        mid = (l + r) // 2
        root = TreeNode(array[mid])
        root.left = create_node(l, mid - 1)
        root.right = create_node(mid + 1, r)
        return root

    return create_node(0, len(array) - 1)


def invert_binary_tree(array):
    root = create_binary_tree(array)
    print("Binary tree before inversion")
    print(print_binary_tree_level_order(root))

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        node.left, node.right = node.right, node.left

    dfs(root)
    print("Binary tree after inversion")
    print(print_binary_tree_level_order(root))


def print_binary_tree_level_order(root):
    if not root:
        return

    q = collections.deque()
    q.append(root)
    node_list = []

    while q:
        q_len = len(q)
        level_nodes = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level_nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)
        node_list.append(level_nodes)
    return node_list


invert_binary_tree([1, 2, 3, 4, 6, 7, 9])
