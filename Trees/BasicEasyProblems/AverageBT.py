from collections import deque

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            levelSum = 0
            n = len(q)

            for i in range(n):
                node = q.popleft()
                levelSum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(levelSum / n)

        return res
    
    