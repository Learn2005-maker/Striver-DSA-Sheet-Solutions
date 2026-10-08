from collections import deque
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        q=deque([root])
        while q:
            summ=0
            for i in range(len(q)):
                node=q.popleft()
                summ+=node.val
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return summ
