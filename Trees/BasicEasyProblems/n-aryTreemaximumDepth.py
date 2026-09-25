class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root is None:
            return 0

        maxHeight = 0

        for child in root.children:
            maxHeight = max(maxHeight, self.maxDepth(child))

        return 1 + maxHeight


# Create the tree

root = Node(1)

node3 = Node(3)
node2 = Node(2)
node4 = Node(4)

node5 = Node(5)
node6 = Node(6)

# Connect children

root.children = [node3, node2, node4]

node3.children = [node5, node6]


# Find maximum depth

solution = Solution()

print(solution.maxDepth(root))