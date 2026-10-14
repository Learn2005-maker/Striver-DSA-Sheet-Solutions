class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)
        curr=root # copy of root beacuse we must return root so root is not destroyed
        while True:
            if curr.val<=val:
                if curr.right:
                    curr=curr.right
                else:
                    curr.right=TreeNode(val)
                    break
            else:
                if curr.left:
                    curr=curr.left
                else:
                    curr.left=TreeNode(val)
                    break

        return root
# Time complexcity:  O(log n)