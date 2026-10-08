
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def dfs(root):
    if not root:
        return []
    
    st=[(root,str(root.val))]
    ans=[]
    while st:
        node,path=st.pop()

        if not node.left and not node.right:
            ans.append(path)
        if node.left:
            st.append((node.left,path +"->"+ str(node.left.val)))
        if node.right:
            st.append((node.right,path +"->"+ str(node.right.val)))
    return ans



        
root=TreeNode(1)

root.left=TreeNode(2)
root.right=TreeNode(3)

root.left.left=TreeNode(8)
root.right.right=TreeNode(10)

result=dfs(root)

print(result)

# ans=[]

# for path in result:
#     parts=path.split("->")
#     newpath=[]

#     for i in parts:
#         newpath.append(int(i))
#     ans.append(newpath)
# print(ans)



