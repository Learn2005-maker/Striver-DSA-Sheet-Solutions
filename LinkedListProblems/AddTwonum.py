class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convertoLL(arr):
    head = Node(arr[0])
    temp=head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        temp.next = new_node
        temp = new_node
    return head    
    
def printLL(head):
    temp=head
    while temp:
        print(temp.data,end=" -> ")
        temp=temp.next
    print(None)
    return head
    
arr=[9,9,9]
arr1=[9,9,9]

head=convertoLL(arr)
head2=convertoLL(arr1)
printLL(head)
printLL(head2)
print("---------------------")
def addTwo(head,head2):
    t1=head
    t2=head2
    dummynode=Node(-1)
    curr=dummynode
    carry=0
    while t1 or t2:
        sum=carry
        if t1:
            sum=sum+t1.data
        if t2:
            sum=sum+t2.data
        newnode=Node(sum%10)
        carry=sum//10
        curr.next=newnode
        curr=curr.next
        if t1:
            t1=t1.next
        if t2:
            t2=t2.next
    
    if carry:
        newnode=Node(carry)
        curr.next=newnode
    return dummynode.next

head=addTwo(head,head2)

printLL(head)
            
            
        
    