
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left,root.right=root.right,root.left

        return root