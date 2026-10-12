class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:        
    def minimumOfBST(root):
        if root is None:
            return float("inf")
        current=root
        while current.left is not None:
            current=current.left
        return current.val
    
    
# Operation	Time Complexity	Auxiliary Space
# Find minimum	O(H)	O(1)
# Find maximum	O(H)	O(1)