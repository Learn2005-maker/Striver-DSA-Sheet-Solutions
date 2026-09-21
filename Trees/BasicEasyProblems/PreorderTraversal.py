class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
# PreOrder
def preOrder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)


root=TreeNode(1)

root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(8)
root.right.right=TreeNode(10)

preOrder(root)