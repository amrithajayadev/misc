# https://leetcode.com/problems/path-sum-ii/

class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(8)
root.right.left = Tree(7)


def find_path_sum(root, target_sum, node_list, paths_list):
    if root:
        if not root.left and not root.right and target_sum==root.val:
            node_list.append(root.val)
            paths_list.append(node_list)
        find_path_sum(root.left, target_sum-root.val, node_list+[root.val], paths_list )
        find_path_sum(root.right, target_sum-root.val, node_list+[root.val], paths_list)

def path_lists_matching_targetsum(root, target_sum):
    paths_list = []
    find_path_sum(root, target_sum, [], paths_list)
    print(paths_list)

path_lists_matching_targetsum(root, 11)