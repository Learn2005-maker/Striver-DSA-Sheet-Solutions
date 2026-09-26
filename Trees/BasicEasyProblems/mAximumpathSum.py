
class Solution:
    def maxPathSum(root):
        maxi=[float("-inf")]

        def maxPath(node):
            if node is None:
                return 0
            
            leftSum=max(0,maxPath(node.left))
            rightSum=max(0,maxPath(node.right))
            maxi[0]=max(maxi[0],node.val+leftSum+rightSum)
            return node.val+max(leftSum,rightSum)
        maxPath(root)
        return maxi[0]