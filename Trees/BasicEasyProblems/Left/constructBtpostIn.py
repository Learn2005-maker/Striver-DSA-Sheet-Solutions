

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if len(inorder)!=len(postorder):
            return None
        def buildnewTree(postorder,ps,pe,inorder,ist,ie,mp):
            if ps>pe or ist>ie:
                return None
            root=TreeNode(postorder[pe])
            inroot=mp[root.val]
            numsleft=inroot-ist

            root.left=buildnewTree(postorder,ps,ps+numsleft-1,inorder,ist,inroot-1,mp)
            root.right=buildnewTree(postorder,ps+numsleft,pe-1,inorder,inroot+1,ie,mp)

            return root
        mp={}
        for i in range(len(inorder)):
            mp[inorder[i]]=i

        root=buildnewTree(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,mp)
        return root