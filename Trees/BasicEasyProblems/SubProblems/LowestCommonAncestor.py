
# Brute Force : O (n) + o(n)
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findPath(root, target):
    if not root:
        return []

    st = [(root, [root.val])]

    while st:
        node, path = st.pop()

        if node.val == target:
            return path

        if node.right:
            st.append((node.right, path + [node.right.val]))

        if node.left:
            st.append((node.left, path + [node.left.val]))

    return []




        
root=TreeNode(1)

root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

root.right.left=TreeNode(8)
root.right.right=TreeNode(9)

path1=findPath(root,4)
path2=findPath(root,8)
print(path1, path2)
ans=[]



i=0

while i<len(path1) and i<len(path2) and path1[i]==path2[i]:
    i+=1


print("Least common Ancestor : ",path1[i-1])

# Time complexity:O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None or p == root  or q ==root:
            return root
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
        
        
        
        
