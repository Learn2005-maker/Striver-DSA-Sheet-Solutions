

def InOrderTraversal(root):
    stack = []
    inorder = []
    node = root

    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            inorder.append(stack.pop().val)
            node = node.right
    return inorder

# Time complexity: O(n) and S.c : O(n)