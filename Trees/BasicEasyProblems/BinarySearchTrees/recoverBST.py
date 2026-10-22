class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder=[]
        st=[]
        cur=root
        while st or cur:
            while cur:
                st.append(cur)
                cur=cur.left
            cur=st.pop()
            inorder.append(cur)
            cur=cur.right
        first=None
        sec=None
        for i in range(1,len(inorder)):
            if inorder[i-1].val>inorder[i].val:
                if first is None:
                    first=inorder[i-1]
                sec=inorder[i]
        if first and sec:
            first.val , sec.val =sec.val,first.val
            
            
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        self.prev=TreeNode(float("-inf"))
        self.first=None
        self.last=None
        self.middle=None
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            if self.prev!=None and self.prev.val>root.val:
                if self.first is None:
                    self.first=self.prev
                    self.middle=root
                else:
                    self.last=root
            self.prev=root
            inorder(root.right)
        inorder(root)
        if self.first and self.last:
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first and self.middle:
            self.first.val,self.middle.val=self.middle.val,self.first.val