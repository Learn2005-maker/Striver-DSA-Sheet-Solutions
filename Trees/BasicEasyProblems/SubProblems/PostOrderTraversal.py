class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
# PreOrder
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    # ans.append(root.data)
    print(root.data)



root=TreeNode(1)

root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(8)
root.right.right=TreeNode(10)

postOrder(root)