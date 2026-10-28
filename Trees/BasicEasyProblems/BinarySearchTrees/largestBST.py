

class NodeValue:
    def __init__(self, minval, maxval, maxsize):
        self.minval = minval
        self.maxval = maxval
        self.maxsize = maxsize


class Solution:
    def largestBst(self, root):
        def largestBST(root):
            if root is None:
                return NodeValue(float("inf"), float("-inf"), 0)

            left = largestBST(root.left)
            right = largestBST(root.right)

            if left.maxval < root.data < right.minval:
                return NodeValue(
                    min(root.data, left.minval),
                    max(root.data, right.maxval),
                    left.maxsize + right.maxsize + 1
                )

            return NodeValue(
                float("-inf"),
                float("inf"),
                max(left.maxsize, right.maxsize)
            )

        return largestBST(root).maxsize
