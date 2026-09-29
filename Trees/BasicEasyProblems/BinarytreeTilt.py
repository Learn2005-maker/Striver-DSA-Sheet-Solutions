
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self,root):
        tilt_sum=0
        def dfs(node):
            nonlocal tilt_sum
            if node is None:
                return 0
            L=dfs(node.left)
            R=dfs(node.right)
            tilt_sum+=abs(L-R)
            return node.val+L+R
        dfs(root) 
        return tilt_sum
    
s=Solution()

root=TreeNode(1)

root.left=TreeNode(2)

root.right=TreeNode(3)


print(s.findTilt(root))