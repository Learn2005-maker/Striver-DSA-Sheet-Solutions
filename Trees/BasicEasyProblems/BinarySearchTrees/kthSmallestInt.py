class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        def dfs(root):
            if root is None:
                return 0
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

            ans.sort()
        ans=[]
        dfs(root)


        return ans[k-1]
    
# but take o(n)+O(nlogn)   time complexity and O(n) space complexity

# here we can do it in O(n) time complexity and O(h) space complexity where h is the height of the tree
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            return 0
        node=root
        st=[]
        count=0
        while True:
            if node:
                st.append(node)
                node=node.left
            else:
                if not st:
                    break
                node=st.pop()
                count+=1
                if count==k:
                    return node.val
                node=node.right
