
class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

from collections import deque
def BottomsideView(root):
    if not root:
        return []

    q=deque([(root,0)])
    mp={}
    while q:
        n=len(q)
        for i in range(n):
            node,line=q.popleft()
            mp[line]=node.data

            if node.left:
                q.append((node.left,line-1))
            if node.right:
                q.append((node.right,line+1))
        
    ans=[]

    for line,node in sorted(mp.items()):
        ans.append(node)
    return ans



root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(8)
root.right.right=TreeNode(10)

print(BottomsideView(root))