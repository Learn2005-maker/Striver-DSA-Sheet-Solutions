class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return
        while root and root.val!=val:
            root=root.left if root.val>val else root.right

        return root
 
