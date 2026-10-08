
from collections import deque

class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def findHeightLeft(node):
            height=0

            while node:
                node=node.left
                height+=1
            return height
        def findHeightRight(node):
            height=0
            while node:
                node=node.right
                height+=1
            return height
        if root is None:
            return 0
        lh=findHeightLeft(root)
        rh=findHeightRight(root)

        if lh==rh:
            return (1<<lh)-1  # (1<<h) =  2**h-1  formula
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        