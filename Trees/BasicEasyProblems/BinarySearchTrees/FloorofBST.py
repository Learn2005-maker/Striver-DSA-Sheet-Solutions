
def FloorOFBST(root,key):
    floor=-1
    if root is None:
        return -1
    
    while root:
        if root.val==key:
            floor=root.val
            return floor
        elif root.val>key:
            root=root.left
        else:
            floor=root.val
            root=root.right
    return floor


# Time complxity:O(log n)
