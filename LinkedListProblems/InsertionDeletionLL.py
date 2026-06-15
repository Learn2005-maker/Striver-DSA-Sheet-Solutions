class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=[10,20,30,40]
head=Node(arr[0])

temp=head

for i in range(1,len(arr)):
    new_node=Node(arr[i])
    temp.next=new_node
    temp=new_node
def print_LL(head):    
    temp=head
    while temp:
        print(temp.data,end=" -> ")
        temp=temp.next
    print("None")

print_LL(head)

# Insertion at Head
def insertatBeg(head,value):
    new_node=Node(value)
    new_node.next=head
    head=new_node
    return head
ans=insertatBeg(head,5) 
print_LL(ans)
# Insertion At Tail
def insertatTail(head,value):
    new_node=Node(value)
    if head is None:
        return new_node
    temp=head    
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
    
ans=insertatTail(head,100)
print_LL(ans)


# Insert at position
def insertatPos(head,pos,value):
    new_node=Node(value)
    if pos==0:
        new_node.next=head
        return new_node
    temp=head
    for i in range(pos-1):
        temp=temp.next
    new_node.next=temp.next
    temp.next=new_node
    return head
insertatPos(head,3,143)
print_LL(head)

    
#Deletion 
def delete_head(head):
    if head is None:
        return None
    head=head.next
    return head


def delete_tail(head):
    if head is None or head.next is None:
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
delhead=delete_head(head)    
print_LL(delhead)

deltail=delete_tail(head)
print_LL(delhead)

# delete at position
def deleteatPos(head,pos):
    if head is None:
        return None
    if pos==0:
        return head.next
    temp=head
    for i in range(pos-1):
        temp=temp.next
    temp.next=temp.next.next
    return head    
delPos=deleteatPos(head,2)
print_LL(delPos)
        


# Insertion and Deletion in Linked List based on value 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
head=ListNode(10)
secound=ListNode(20)
third=ListNode(30)

head.next=secound
secound.next=third

# temp=head

def print_LL(head):
    temp=head
    while temp:
        print(temp.val,end=" -> ")
        temp=temp.next
    print("None")    
    return head
    
def insertatValue(head,target,value):
    new_node=ListNode(value)
    temp=head
    while temp:
        if temp.val==target:
            new_node.next=temp.next
            temp.next=new_node
            break
        temp=temp.next
    return head

insertatValue(head,20,25)    
print_LL(head)

def delete_value(head,value):
    if head is None:
        return None
    if head.val==value:
        return head.next
    temp=head
    while temp.next:
        if temp.next.val==value:
            temp.next=temp.next.next
            break
        temp=temp.next
    return head
delete_value(head,25)
print_LL(head)    
        

        
        

        