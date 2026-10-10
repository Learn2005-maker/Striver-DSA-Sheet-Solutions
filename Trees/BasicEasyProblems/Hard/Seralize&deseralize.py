from collections import deque

class Codec:

    def serialize(self, root):
        if root is None:
            return ""
        q=deque([root])
        s=""
        while q:
            node=q.popleft()
            if node==None:
                s+='#'+','
            else:
                s=s+str(node.val)+','
            if node!=None:
                q.append(node.left)
                q.append(node.right)
        return s
    def deserialize(self, data):
        if len(data)==0:
            return None
        s=data.split(',')
        root=TreeNode(int(s[0]))
        q=deque([root])
        i=1
        while q:
            node=q.popleft()
            if s[i]=='#':
                node.left=None
            else:
                leftNode=TreeNode(int(s[i]))
                node.left=leftNode
                q.append(node.left)
            i+=1
            if s[i]=='#':
                node.right=None
            else:
                rightNode=TreeNode(int(s[i]))
                node.right=rightNode
                q.append(node.right)
            i+=1
        return root

