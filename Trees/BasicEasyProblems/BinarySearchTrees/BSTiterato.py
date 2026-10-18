# time complxity:O(1) and space complexity:O(n)
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.arr=[]
        self.index=0
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(root)

    def next(self) -> int:
        val=self.arr[self.index]
        self.index+=1
        return val

    def hasNext(self) -> bool:
        return len(self.arr)>self.index
    
    
    
    
    



        