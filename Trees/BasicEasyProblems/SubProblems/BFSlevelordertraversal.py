from collections import deque

def levelOrder(root):
    ans=[]
    if root is None:
        return ans
    q=deque()
    q.append(root)
    while q:
        n=len(q)
        level=[]
        for i in range(n):
            node=q.popleft()
            if node.left :
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        ans.append(level)
    return ans
