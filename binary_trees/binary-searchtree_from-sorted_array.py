from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def sortedArrayToBST(nums):
    l = 0
    r = len(nums)
    root = create_tree_node(nums, l, r - 1)
    # preorder_traversal(root)
    output = level_order_traversal(root)

    return output


def create_tree_node(nums, l, r):
    if l > r:
        return
    mid = (l + r) // 2
    root = TreeNode(nums[mid])
    if root is not None:
        root.left = create_tree_node(nums, l, mid - 1)
        root.right = create_tree_node(nums, mid + 1, r)
        return root


def find_height(root):
    if root is None:
        return 0
    else:
        l_height = 1 + find_height(root.left)
        r_height = 1 + find_height(root.right)
        return max(r_height, l_height)


def get_level_nodes(node, h, node_list):
    if node is None:
        node_list.append(None)
        return
    if h == 1:
        node_list.append(node.value)
    else:
        get_level_nodes(node.left, h - 1, node_list)
        get_level_nodes(node.right, h - 1, node_list)


def level_order_traversal(root):
    h = find_height(root)
    node_list = []
    for i in range(1, h + 1):
        get_level_nodes(root, i, node_list)
    return node_list


def get_level_nodes1(node, i, l, nodelist):
    if i == l:
        nodelist.append(node)
        print(f"node value {node.value} at level:{i}")
        return nodelist
    get_level_nodes1(node.left, i + 1, l, nodelist)
    get_level_nodes1(node.right, i + 1, l, nodelist)
    return


def test_my_level_nodes(nums):
    l = 0
    r = len(nums) - 1
    root = create_tree_node(nums, l, r)
    node_list = []
    # print(get_level_nodes1(root, 0, 2, node_list))
    print(node_list)
    print(level_order_traversal_queue(root))


def level_order_traversal_queue(node):
    if not node:
        return
    all_nodes = []
    queue = deque()
    queue.append(node)
    while queue:
        q_len = len(queue)
        l_nodes = []
        for i in range(q_len):
            n = queue.popleft()
            if n:
                l_nodes.append(n.value)
                queue.append(n.left)
                queue.append(n.right)
        all_nodes.append(l_nodes)
    return all_nodes


test_my_level_nodes(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
test_my_level_nodes(nums=[1, 2, 3])


# print(sortedArrayToBST(nums=[-10, -3, 0, 5, 9]))
def create_tree():
    # level order : Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
    root = TreeNode(1)
    root.left = TreeNode(10)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(12)
    root.left.left.right = TreeNode(8)

    root.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.left.right = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(2)
    return level_order_traversal_queue(root)


print(create_tree())


def even_and_is_decreasing(nums):
    if len(nums) == 1:
        if nums[0] % 2 == 0:
            return True
        else:
            return False
    for i in range(1, len(nums)):
        if (nums[i] > nums[i - 1]) or nums[i] % 2 != 0 or nums[i - 1] % 2 != 0:
            return False
    return True


print(even_and_is_decreasing([10, 4]))
