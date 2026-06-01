class Node:
    def __init__(self,val,next=None,prev=None):
        self.data=val
        self.next=None
        self.prev=None
        
head=Node(10)
secound=Node(20)
third=Node(30)

head.next=secound
secound.prev=head

secound.next=third
third.prev=secound

def printforward(head):
    temp=head
    while temp:
        print(temp.data,end=" <-> ")
        temp=temp.next
    print("None")    
    return head
    
printforward(head)    
# Reverse a DLL
def reverseDLL(head):
    if head is None:
        return None
    curr= head 
    last=None
    while curr:
        curr.next,curr.prev=curr.prev,curr.next
        last=curr
        curr=curr.prev

    return last
    
head=reverseDLL(head)    
printforward(head)



# Reverse a DLL using Stack
# Time Complexity: O(2n) and Space Complexity: O(n)
def reverseDLL(head):
    if head is None:
        return None
        
    stack=[]
    temp=head
    while temp:
        stack.append(temp.data)
        temp=temp.next
    
    temp=head
    while temp:
        temp.data=stack.pop()
        temp=temp.next
    return head
head=reverseDLL(head)
printforward(head)    