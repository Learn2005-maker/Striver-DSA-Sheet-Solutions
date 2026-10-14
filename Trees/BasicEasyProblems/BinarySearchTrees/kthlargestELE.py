
class Solution:
    def kthLargest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        count = 0
        node = root

        while True:
            if node:
                stack.append(node)
                node = node.right
            else:
                if not stack:
                    break
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                node = node.left
