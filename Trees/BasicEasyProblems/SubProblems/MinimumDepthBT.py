from collections import deque
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        q=deque()
        q.append(root)
        depth=1
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left == None and node.right==None:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth+=1
        return depth