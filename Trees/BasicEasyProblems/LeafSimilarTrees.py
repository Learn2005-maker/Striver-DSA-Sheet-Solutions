
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        
        def collect_leaves(root,leaves):
            if root is None:
                return 
            if not root.left and not root.right:
                leaves.append(root.val)
            collect_leaves(root.left,leaves)
            collect_leaves(root.right,leaves)
        leaf1=[]
        leaf2=[]
        collect_leaves(root1,leaf1)
        collect_leaves(root2,leaf2)
        return leaf1==leaf2
    

root1=TreeNode(1)

root1.left=TreeNode(2)
root1.right=TreeNode(3)

root1.left.left=TreeNode(8)
root1.right.right=TreeNode(10)


root1.left.right=TreeNode(7)
root1.right.left=TreeNode(10)



root2=TreeNode(1)

root2.left=TreeNode(2)
root2.right=TreeNode(3)

root2.left.left=TreeNode(8)
root2.right.right=TreeNode(10)


root2.left.right=TreeNode(7)
root2.right.left=TreeNode(10)

s=Solution()

print(s.leafSimilar(root1,root2))

