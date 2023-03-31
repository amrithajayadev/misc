class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_BT(arr):
    root = TreeNode(val=5)
    root.left = TreeNode(val=4)
    root.right = TreeNode(val=8)
    root.left.left = TreeNode(val=11)
    root.left.left.left = TreeNode(val=7)
    root.left.left.right = TreeNode(val=2)
    root.right.left = TreeNode(val=13)
    root.right.right = TreeNode(val=4)
    root.right.right.right = TreeNode(val=1)
    return root


def validate_binary_tree(root, l, r):
    if root is None:
        return True
    if not l < root.val < r:
        return False
    return validate_binary_tree(root.right, root.val, r) and validate_binary_tree(root.left, l, root.val)


root = create_BT([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])


# if validate_binary_tree(root, float('-inf'), float('inf')):
#     print("True")
# else:
#     print("False")

def path_sum(node, sum, targetSum):
    if sum == targetSum:
        print(f"sum:{sum}")
        return True
    node.val += sum
    if node.left:
        path_sum(node.left, node.val, targetSum)
    if node.right:
        path_sum(node.right, node.val, targetSum)


def path_sum1(node, targetSum):
    if node.val == targetSum:
        print(node.val)
        return True
    if node.left:
        node.left.val += node.val
        path_sum1(node.left, targetSum)
    if node.right:
        node.right.val += node.val
        path_sum1(node.right, targetSum)
    return


leaves = []


def get_leaves(root, leaves):
    if root.left:
        get_leaves(root.left, leaves)
    if root.right:
        get_leaves(root.right, leaves)
    if root.left is None and root.right is None:
        print(root.val)
        leaves.append(root.val)


# print(path_sum(root, 0, 22))
if path_sum1(root, 22):
    print("True")
else:
    print("False")
# print(path_sum1(root, 22))
# get_leaves(root, leaves)
# print(leaves)