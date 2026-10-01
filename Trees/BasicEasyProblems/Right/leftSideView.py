
# Definition for a binary tree node.
# class TreeNode:
                                 #     def __init__(self, val=0, left=None, right=None):
#     self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
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
