from operator import pos


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create DLL from array
def create_dll(arr):

    # Empty array
    if len(arr) == 0:
        return None

    # Create head node
    head = Node(arr[0])

    temp = head

    # Create remaining nodes
    for i in range(1, len(arr)):

        new_node = Node(arr[i])

        temp.next = new_node
        new_node.prev = temp

        temp = new_node

    return head


# Print DLL forward
def print_forward(head):

    temp = head

    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next

    print("None")


# Print DLL backward
def print_backward(head):

    temp = head

    # Move to tail
    while temp.next:
        temp = temp.next

    # Traverse backward
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.prev

    print("None")


# Array
arr = [10, 20, 30, 40, 50]

# Create DLL
head = create_dll(arr)

print("Forward Traversal:")
print_forward(head)

print("Backward Traversal:")
print_backward(head)

# insertion at head
def insert_head(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    head=new_node
    return head

print("After Inserting 5 at head:")
head=insert_head(head,5)
print_forward(head)

# insert at tail
def insert_tail(head,data):
    new_node=Node(data)
    temp=head
    if head is None:
        return new_node
    while temp.next:
        temp=temp.next
    temp.next=new_node
    new_node.prev=temp
    return head
head=insert_tail(head,400)
print_forward(head)    



def insertatPos(head,data,pos):
    new_node=Node(data)
    if pos==0:
        new_node.next=head
        if head:
            head.prev=new_node
        return new_node
    temp=head
    for i in range(pos-1):
        temp=temp.next
    new_node.next=temp.next
    if temp.next:
        temp.next.prev=new_node
    temp.next=new_node    
    new_node.prev=temp
    
    return head
head =insertatPos(head,47,4)        
print_forward(head)        

# Deletion
# Delete at Head
def delete(head):
    if head is None:
        return None
    if head.next is None:
        return None
    head=head.next
    head.prev=None
    return head
head=delete(head)
print_forward(head)

# Delete at Tail

def deleteTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    temp=head
     
    while temp.next:
        temp=temp.next
    
    temp.prev.next=None
    temp.prev=None    
    return head
head=deleteTail(head)
print_forward(head)  

def deleteatPos(head,pos):
    temp=head
    if  head is None:
        return None
    if pos==0:
        if head.next==None:
            return None
        head=head.next 
        head.prev=None
    for i in range(pos):
        temp=temp.next
    temp.next.prev=temp.prev
    temp.prev.next=temp.next
    temp.prev=None
    temp.next=None
    return head
head=deleteatPos(head,3)   
print_forward(head)
          
          



        