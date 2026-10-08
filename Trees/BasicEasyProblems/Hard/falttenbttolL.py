# Using Recursive approach using RIGHT LEFT ROOT  .(Reverse post order)
class Solution:
    def __init__(self):
        self.prev=None
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        right=self.flatten(root.right)
        left=self.flatten(root.left)
        root.right=self.prev
        root.left=None
        self.prev=root


# Itervative Appraoch



class Solution:
    def __init__(self):
        self.st = []

    def flatten(self, root: TreeNode | None) -> None:
        if root is None:
            return

        self.st.append(root)

        while self.st:
            node = self.st.pop()

            if node.right:
                self.st.append(node.right)

            if node.left:
                self.st.append(node.left)

            if self.st:
                node.right = self.st[-1]

            node.left = None
            
            
# 3rd Approach


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        curr=root
        while curr:
            if curr.left:
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right
    