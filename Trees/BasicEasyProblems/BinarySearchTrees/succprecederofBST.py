



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def predBST(self, root, key):
        predecessor = -1
        st = []

        while root or st:
            if root:
                st.append(root)
                root = root.left
            else:
                root = st.pop()

                if root.val < key:
                    predecessor = root.val
                else:
                    return predecessor

                root = root.right

        return predecessor


values = [20, 10, 30, 5, 15, 25, 35]
key = 20

sol = Solution()
root = None

# Build the BST from the list
for val in values:
    root = sol.insert(root, val)

# Find and display the predecessor
result = sol.predBST(root, key)
print("Inorder Predecessor:", result)









# Time complxity: O(n) and S.c : O(1)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def succBST(self, root, key):
        successor = -1
        st = []

        while root or st:
            if root:
                st.append(root)
                root = root.left
            else:
                root = st.pop()

                if root.val > key:
                    return root.val

                root = root.right

        return successor


values = [20, 10, 30, 5, 15, 25, 35]
key = 20

sol = Solution()
root = None

# Build the BST
for val in values:
    root = sol.insert(root, val)

# Find and display the successor
result = sol.succBST(root, key)
print("Inorder Successor:", result)



# Optimal logic take s O(log n) and O(H)
def succBST(self, root, key):
        successor= -1

        while root:
            if root.val<=key:
                root=root.right
            else:
                successor=root.val
                root=root.left
        return successor
    

def preBST(self, root, key):
        predecessor= -1

        while root:
            if root.val<key:
                predecessor=root.val
                root=root.right
            else:
                root=root.left 
        return predecessor 