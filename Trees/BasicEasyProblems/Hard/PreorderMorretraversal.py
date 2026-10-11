
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        preorder=[]
        cur=root

        while cur:
            if cur.left==None:
                preorder.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if prev.right==None:
                    prev.right=cur
                    preorder.append(cur.val)
                    cur=cur.left
                else:
                    prev.right==None
                    cur=cur.right
        return preorder