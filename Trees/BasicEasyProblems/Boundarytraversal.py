
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isLeaf(node):
    if not node.left and not node.right:
        return True
    return False


def addLeftboundary(root, res):
    node = root.left

    while node:
        if not isLeaf(node):
            res.append(node.val)

        if node.left:
            node = node.left
        else:
            node = node.right


def addRightboundary(root, res):
    temp = [] 
    node = root.right

    while node:
        if not isLeaf(node):
            temp.append(node.val)

        if node.right:
            node = node.right
        else:
            node = node.left

    temp.reverse()

    for value in temp:
        res.append(value)


def addleafs(root, res):
    if isLeaf(root):
        res.append(root.val)
        return

    if root.left:
        addleafs(root.left, res)

    if root.right:
        addleafs(root.right, res)


def boundary(root):
    res = []

    if root is None:
        return []

    # Root
    if not isLeaf(root):
        res.append(root.val)

    # Left boundary
    addLeftboundary(root, res)

    # Leaf nodes
    addleafs(root, res)

    # Right boundary
    addRightboundary(root, res)

    return res


# Creating the tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(7)

root.left.right.left = Node(8)
root.left.right.right = Node(9)


# Boundary Traversal

# print(boundary(root))
# ```

# ### Tree

# ```text
#              1
#            /   \
#           2     3
#          / \     \
#         4   5     7
#            / \
#           8   9
# ```

# ### Output

# ```text
# [1, 2, 4, 8, 9, 7, 3]
# ```

# Notice the four parts:

# ```text
# Root
#  ↓
# 1

# Left Boundary
#  ↓
# 2

# Leaf Nodes
#  ↓
# 4 → 8 → 9 → 7

# Right Boundary (reverse)
#  ↓
# 3
# ```

# So:

# ```text
# 1 → 2 → 4 → 8 → 9 → 7 → 3
# ```

# **Important:** `5` is not included because it is neither a leaf nor part of the outer left/right boundary.
