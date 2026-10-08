class TreeNode:
    def __init__(self,val):
        self.data=val
        self.children=[]


root=TreeNode(1)
root.children=[TreeNode(4),TreeNode(6),TreeNode(10)]


# N-Binary Tree PreOrder Traversal
def preorder(root):
    ans=[]
    if root is None:
        return ans
    ans.append(root.data)
    for child in root.children:
        ans.extend(preorder(child))
    return ans


print(preorder(root))