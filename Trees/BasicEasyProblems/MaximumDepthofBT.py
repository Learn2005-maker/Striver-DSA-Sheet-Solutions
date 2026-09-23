class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def maxD(root):
            if root is None:
                return 0
            lmax=maxD(root.left)
            rmax=maxD(root.right)
            return 1+max(lmax,rmax)
        return maxD(root)
        