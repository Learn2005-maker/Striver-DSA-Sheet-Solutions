def convertoVertical(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    temp = head

    for i in range(1, len(arr)):
        newnode = Node(arr[i])
        temp.child = newnode
        temp = temp.child

    return head


temp = head
arr = []

while temp:
    t2 = temp
    while t2:
        arr.append(t2.data)
        t2 = t2.child
    temp = temp.next

arr.sort()

head = convertoVertical(arr)
