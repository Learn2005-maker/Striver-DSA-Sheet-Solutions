class Solution:
    def postorder(self, root: 'Node'):
        ans=[]
        if root is None:
            return 
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans
