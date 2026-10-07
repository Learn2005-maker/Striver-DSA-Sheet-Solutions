
from collections import deque


class Solution:
    def timetoburnTree(root,target):
        def parentTonode(root,target,parent_track):
            q=deque([root])
            while q:
                node=q.popleft()
                if node.left:
                    parent_track[node.left]=node
                    q.append(node.left)
                if node.right:
                    parent_track[node.right]=node
                    q.append(node.right)
  
        if not root:
            return 0
        parentTonode(root,target,parent_track)
        visited={}
        q=deque([target])
        time=0
        while q:
            burned=False
            for i in range(len(q)):
                node=q.popleft()
                if node.left and  node.left not in visited:
                    q.append(node.left)
                    visited[node.left]=True
                    burned=True
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited[node.right]=True
                    burned=True
                if node in parent_track and parent_track[node] not in visited:
                    q.append(parent_track[node])
                    visited[parent_track[node]]=True
                    burned=True
            if burend:
                time+=1


        return time if time>=1 else 0
