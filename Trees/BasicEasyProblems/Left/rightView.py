
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        stack=[]
        def dfs(node,level):
            if node is None:
                return
            if len(stack)==level:
                stack.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root,0)
        return stack
