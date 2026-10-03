class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root1,root2):
            if root1 is None:
                return 
            if root1==target:
                return root2
            return dfs(root1.left,root2.left) or  dfs(root1.right,root2.right)
        
        return dfs(original,cloned)