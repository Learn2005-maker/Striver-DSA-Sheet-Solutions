def preorderTraversal(root):
    stack = []
    stack.append(root)

    ans = []

    while stack:
        node = stack.pop()

        ans.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return ans

preorderTraversal(root)