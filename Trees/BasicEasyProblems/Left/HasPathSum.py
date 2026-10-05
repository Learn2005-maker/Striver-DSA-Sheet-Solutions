class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(root,targetSum):
            if root is None:
                return False
            st=[(root,[root.val])]
            while st:
                node,path=st.pop()
                if not node.left and not node.right:
                    if sum(path)==targetSum:
                        return True
                if node.left:
                    st.append((node.left,path+[node.left.val]))
                if node.right:
                    st.append((node.right,path+[node.right.val]))
            return False
        return dfs(root,targetSum)
            


        