# Time complxity:  O(HEight of Tree)  which is O(log n) for balanced tree and O(n) for skewed tree
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        def helper(root):
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            rightChild=root.right
            lastRight=findlastright(root.left)
            lastRight.right=rightChild
            return root.left


        def findlastright(root):
            if root.right==None:
                return root
            return findlastright(root.right)




        if root is None:
            return None
        if root.val==key:
            return helper(root)
        dummy=root
        while root:
            if root.val>key:
                if root.left and root.left.val==key:
                    root.left= helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=helper(root.right)
                    break
                else:
                    root=root.right              
        return dummy 