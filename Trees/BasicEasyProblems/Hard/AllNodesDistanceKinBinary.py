
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x                                      
#         self.left = None 
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def  marksParents(node,target,parent_track):
            q=deque([root])
            while q:
                node=q.popleft()
                if node.left:
                    parent_track[node.left]=node
                    q.append(node.left)
                if node.right:
                    parent_track[node.right]=node 
                    q.append(node.right)
        parent_track={}
        marksParents(root,target,parent_track)
        visited={}
        q=deque([target])
        visited[target]=True  
        curr_level=0
        while q:
            size=len(q)
            if curr_level==k:
                break
            curr_level+=1
            for i in range(size):
                node=q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited[node.left]=True
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited[node.right]=True
                if node in parent_track and parent_track[node] not in visited:
                    q.append(parent_track[node])
                    visited[parent_track[node]]=True
        result=[]
        while q:
            node=q.popleft()
            result.append(node.val)

        return result





        