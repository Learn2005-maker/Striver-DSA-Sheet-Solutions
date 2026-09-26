# Brute Force Approach
# Time complxity: O (n^2)

class Solution:
    def diameterOfBinaryTree(self, root) :
        def Height(node):
            if node is None:
                return 0
            
            lh=Height(node.left)
            rh=Height(node.right)
            return 1+max(lh,rh)
        if root is None:
            return 0
        maxi=0
        lh=Height(root.left)
        rh=Height(root.right)
        currentD=lh+rh
        leftD=self.diameterOfBinaryTree(root.left)
        rightD=self.diameterOfBinaryTree(root.right)
        return max(currentD,leftD,rightD)

# Optimal Approach
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = [0]

        def Height(node):
            if node is None:
                return 0

            lh = Height(node.left)
            rh = Height(node.right)

            diameter[0] = max(diameter[0], lh + rh)

            return 1 + max(lh, rh)

        Height(root)
        return diameter[0]