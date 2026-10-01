from collections import deque
class Solution:
    def verticalTraversal(self, root):
        if root is None:
            return []
        q=deque()
        mp={}   # column-> nodes
        q.append((root,0,0))

        while q:
            node,row,col=q.popleft()
            if col not in mp:
                mp[col]=[]
            mp[col].append((row,node.val))

            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        ans=[]
        # Columns from left to right
        for col in sorted(mp):
            nodes=mp[col]
            nodes.sort()
            column=[]

            for row,val in nodes:
                column.append(val)

            ans.append(column)

        return ans
