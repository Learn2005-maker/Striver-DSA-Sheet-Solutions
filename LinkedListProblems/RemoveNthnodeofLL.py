class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [1,2,3,4,5]

# Convert array to linked list
head = Node(arr[0])
temp = head

for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node

# Traverse
print("Linked List:")
def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
    return head


   

def delatPos(head,pos):
    if head is None:
        return head
    if  pos==0:
        return head.next
    
    temp=head
    for i in range(pos-1):
        temp=temp.next
    if temp and temp.next is None:
        return head
        
    temp.next=temp.next.next
    return head 

temp=head
length=0
while temp:
    length+=1
    temp=temp.next
print(length)  
n=2
pos=length-n    
    
head=delatPos(head,pos)    
printLL()
        


# Optimal code  pseudo code
# Time complexity O(n) and space complexity O(1)
fast=head
for i in range(n):
    fast=fast.next
if fast is None:
    print(head.next)
slow=head
while fast and fast.next:
    fast=fast.next
    slow=slow.next
slow.next=slow.next.next  


   
