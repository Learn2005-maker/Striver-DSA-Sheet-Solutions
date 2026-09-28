
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=deque()
        q.append(root)
        L_to_R=True
        result=[]
        while q:
            n=len(q)
            cur_level=[]
            for i in range(n):
                node=q.popleft() 
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                 
            if not L_to_R:
                cur_level.reverse()
            L_to_R=not L_to_R
            result.append(cur_level)
        return result   