class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

root=TreeNode(1)

root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(8)
root.right.right=TreeNode(10)

# Basic Implementation of binary tree with 5 nodes

