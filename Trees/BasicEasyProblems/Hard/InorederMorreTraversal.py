
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        inorder=[]
        cur=root

        while cur:
            if cur.left==None:
                inorder.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if prev.right==None:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right==None
                    inorder.append(cur.val)
                    cur=cur.right
        return inorder