# https://leetcode.com/problems/delete-node-in-a-bst/
from misc.binary_trees.binary_trees_traversal import level_order_traversal


class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def create_bst(nums, i):
    if i >= len(nums):
        return

    root = Tree(nums[i])
    if root is not None:
        root.left = create_bst(nums, i+1)
        root.right = create_bst(nums, i+2)
        return root

root = create_bst([5, 3, 6, 2, 4, None, 7], 0)

# level_order_traversal(root)