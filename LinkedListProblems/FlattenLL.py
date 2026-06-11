class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.child = Node(5)  
head.child.child=Node(7)    
     
    
        
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
# OptimLy we can merge the linked list instead of sorting the array and creating a new linked list
def merge(head,mergedhead):
    t1=head
    t2=mergedhead
    dummynode=Node(-1)
    res=dummynode
    while t1 and t2:
        if t1.data<=t2.data:
            res.child=t1
            res=t1
            t1=t1.child
        else:
            res.child=t2
            res=t2
            t2=t2.child
        res.next=None
    if t1:
        res.child=t1
    else:
        res.child=t2
    return dummynode.child    



def flattenLinkedList(head):
    if head is None or  head.next is None:
        return head
    mergedhead=flattenLinkedList(head.next)
    head.next = None
    return merge(head,mergedhead)
    
    
    
    