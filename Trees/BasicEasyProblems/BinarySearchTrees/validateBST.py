class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def isvalid(root,minval,maxval):
            if root is None:
                return True
            if root.val>=maxval or root.val<=minval:
                return False
            return isvalid(root.left,minval,root.val) and isvalid(root.right,root.val,maxval)
        minRange=float("-inf")
        maxRange=float("inf")
        return isvalid(root,minRange,maxRange)
    
    