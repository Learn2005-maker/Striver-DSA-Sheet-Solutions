
def CeilofBST(root,key):
    ceil=-1
    if root is None:
        return -1
    
    while root:
        if root.val==key:
            ceil=root.val
            return ceil
        elif root.val>key:
            ceil=root.val
            root=root.left
        else:
            root=root.right
    return ceil


# Time complxity:O(log n)
