# BUild bst using preorder traversal.
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        i=0
        def buildBST(preorder,ubound):
            nonlocal i
            if i==len(preorder) or preorder[i]>ubound:
                return None
            root=TreeNode(preorder[i])
            i+=1
            root.left=buildBST(preorder,root.val)
            root.right=buildBST(preorder,ubound)
            return root
        int_max=float("inf")
        return buildBST(preorder,int_max)
    
    