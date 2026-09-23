def postOrderTraversal(root):
    st1=[]
    st2=[]
    postoder=[]
    if root is None:
        return postorder
    st1.append(root)
    while st1:
        node=st1.pop()
        st2.append(node)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    
    while st2:
        node=st2.pop()
        postoder.append(node.val)
    return postorder
        

