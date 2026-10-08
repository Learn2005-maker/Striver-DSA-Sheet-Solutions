
from collections import deque
def topsideView(root):
    if not root:
        return []

    q=deque([(root,0)])
    mp={}
    while q:
        n=len(q)
        for i in range(n):
            node,line=q.popleft()
            if line not in mp:
                mp[line]=node.val

            if node.left:
                q.append((node.left,line-1))
            if node.right:
                q.append((node.right,line+1))
        
    ans=[]

    for line,node in sorted(mp.items()):
        ans.append(node.val)
    return ans

