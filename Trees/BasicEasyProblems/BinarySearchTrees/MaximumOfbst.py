
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:        
    def MaximumOfBST(root):
        if root is None:
            return float("-inf")
        current=root
        while current.right is not None:
            current=current.right
        return current.val
