
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        q=deque([root])
        while q:
            n=len(q)
            find_x=False
            find_y=False
            for i in range(n):
                node=q.popleft()
                if node.left and node.right:
                    if ((node.left.val==x and node.right.val==y)or (node.left.val==y and node.right.val==x  )):
                        return False
                if node.val==x:
                    find_x=True
                if node.val==y:
                    find_y=True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if find_x and find_y:
                return True
            if find_x or find_y:
                return False
        return False
