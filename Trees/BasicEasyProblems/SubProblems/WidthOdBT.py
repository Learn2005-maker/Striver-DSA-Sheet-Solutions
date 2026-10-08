from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        q=deque([(root,0)])
        ans=0
        while q:
            n=len(q)
            minI=q[0][1]
            first=0
            last=0

            for i in range(n):
                node,index=q.popleft()
                curI=index-minI
                if i==0:
                    first=curI
                if i==n-1:
                    last=curI
                if node.left:
                    q.append((node.left,2*curI+1))
                if node.right:
                    q.append((node.right,2*curI+2))
            ans=max(ans,last-first+1)
        return ans