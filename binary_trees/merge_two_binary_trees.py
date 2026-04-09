from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_binary_trees(root1, root2):
    def dfs(node1, node2):
        if not node1 and not node2:
            return
        sum = 0
        if node1:
            sum += node1.val
        if node2:
            sum += node2.val
        root = TreeNode(sum)
        root.left = dfs(node1.left if node1 else None, node2.left if node2 else None)
        root.right = dfs(node1.right if node1 else None, node2.right if node2 else None)
        return root

    root = dfs(root1, root2)
    print(print_binary_tree_level_order(root))


def print_binary_tree_level_order(root):
    if not root:
        return
    q = deque()
    q.append(root)
    nodes = []
    while q:
        q_len = len(q)
        level_nodes = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level_nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)
        nodes.append(level_nodes)
    return nodes


def create_binary_tree(arr):
    if not arr:
        return

    def create_node(l, r):
        if l > r:
            return
        mid = (l + r) // 2
        root = TreeNode(arr[mid])
        root.left = create_node(l, mid - 1)
        root.right = create_node(mid + 1, r)
        return root

    return create_node(0, len(arr) - 1)


root1 = create_binary_tree([5, 3, 1, 2])
print(print_binary_tree_level_order(root1))
print("Tree 1 above")
root2 = create_binary_tree([0, 1, 4, 2, 0, 3, 7])
print(print_binary_tree_level_order(root2))
print("Tree 2 above")
merge_binary_trees(root1, root2)
print("Merged Tree above")
