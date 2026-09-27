
class Solution:
    def binaryTreePaths(self, root):
        ans=[]
        if root is None:
            return ans
        stack=[(root,str(root.val))]
        while stack:
            node,path=stack.pop()
            if not node.left and not node.right:
                ans.append(path)

            if node.right:
                stack.append([node.right,path+"->"+str(node.right.val)])
            if node.left:
                stack.append([node.left,path+"->"+str(node.left.val)])
        return ans
        