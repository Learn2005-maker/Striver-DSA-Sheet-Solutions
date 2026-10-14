class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def buildnewTree(preorder,preStart,preEnd,inorder,inStart,inEnd,mp):
            if preStart>preEnd or inStart > inEnd:
                return None
            root=TreeNode(preorder[preStart])
            inroot=mp[root.val]
            numsleft=inroot-inStart

            root.left=buildnewTree(preorder,preStart+1,preStart+numsleft,inorder,inStart,inroot-1,mp)
            root.right=buildnewTree(preorder,preStart+numsleft+1,preEnd,inorder,inroot+1,inEnd,mp)

            return root
        mp={}

        for i in range(len(inorder)):
            mp[inorder[i]]=i

        root=buildnewTree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,mp)
        return root

