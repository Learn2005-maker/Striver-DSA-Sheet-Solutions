
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        st=[]

        for num in nums:
            node=TreeNode(num)

            while st and st[-1].val<num:
                node.left=st.pop()
            if st:
                st[-1].right=node
            st.append(node)
        return st[0]