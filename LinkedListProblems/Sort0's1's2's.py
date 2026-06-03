class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [1,0,2,0,1]

# Convert array to linked list
head = Node(arr[0])
temp = head

for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node

# Traverse
print("Linked List:")

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

temp=head
count0=0
count1=0
count2=0
while temp:
    if temp.data==0:
        count0+=1
    elif temp.data==1:
        count1+=1
    else:
        count2+=1
    temp=temp.next
temp=head
while temp:
    if count0:
        temp.data=0
        count0-=1
    elif count1:
        temp.data=1
        count1-=1
    else:
        temp.data=2
        count2-=1
    temp=temp.next

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    
# Time Complexity: O(n+n) and Space Complexity: O(1)



temp=head
if head is None or head.next is None:
    print(head)
    
zerohead=Node(-1)
onehead=Node(-1)
twohead=Node(-1)
zero=zerohead
one=onehead
two=twohead

while temp:
    if temp.data==0:
        zero.next=temp
        zero=zero.next
    elif temp.data==1:
        one.next=temp
        one=one.next
    else:
        two.next=temp
        two=two.next
    temp=temp.next
zero.next= onehead.next if onehead.next else twohead.next
one.next=twohead.next  
two.next=None
newHead=zerohead.next

temp=newHead
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    

# Time complexcity:O(n) and space : O(1)
    