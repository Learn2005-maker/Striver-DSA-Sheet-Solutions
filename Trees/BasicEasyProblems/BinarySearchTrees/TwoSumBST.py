# time complxity:O(n) and space complexity:O(n)
def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        inorder=[]
        st=[]
        curr=root
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            inorder.append(curr.val)

            curr=curr.right
        i=0
        j=len(inorder)-1

        while i<j:
            total=inorder[i]+inorder[j]
            if total==k:
                return True
            elif total>k:
                j-=1
            else:
                i+=1
        return False
    
from typing import Optional
class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root, reverse):
        self.stack = []
        self.reverse = reverse
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)

            if self.reverse:
                node = node.right  # Largest first
            else:
                node = node.left   # Smallest first

    def next(self):
        node = self.stack.pop()

        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack)!=0


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        left = BSTIterator(root, False)   # Smallest to largest
        right = BSTIterator(root, True)   # Largest to smallest

        i = left.next()
        j = right.next()

        while i < j:
            total = i + j

            if total == k:
                return True

            elif total < k:
                i = left.next()

            else:
                j = right.next()

        return False
if __name__ == "__main__":
    root = TreeNode(7) 
    root.left = TreeNode(3) 
    root.right = TreeNode(15) 
    root.right.left = TreeNode(9) 
    root.right.right = TreeNode(20) 
    k = 12 
    solution = Solution() 
    result = solution.findTarget(root, k) 
    print("Target:", k) 
    print("Pair exists:", result)