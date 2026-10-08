def prepostInOrderTraversal(root):
    pre = []
    In = []
    post = []
    stack = []

    if root is None:
        return pre, In, post

    stack.append([root, 1])

    while stack:
        node, state = stack.pop()

        # State 1 -> Preorder
        if state == 1:
            pre.append(node.val)

            state += 1
            stack.append([node, state])

            if node.left:
                stack.append([node.left, 1])

        # State 2 -> Inorder
        elif state == 2:
            In.append(node.val)

            state += 1
            stack.append([node, state])

            if node.right:
                stack.append([node.right, 1])

        # State 3 -> Postorder
        else:
            post.append(node.val)

    return pre, In, post