class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [1,2,3]

# Convert array to linked list
head = Node(arr[0])
temp = head

for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node
temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)


temp=head
num=0
while temp:
    num=num*10+temp.data
    temp=temp.next
num+=1
print(num)

digits=str(num)

new_head=Node(digits[0])
temp=new_head

for digit in digits[1:]:
    temp.next=Node(digit)
    temp=temp.next
temp=new_head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    
    
    
# Time Complexity: O(N) and Space Complexity: O(N) where n is the number of digits in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [1,2,3]

# Convert array to linked list
head = Node(arr[0])
temp = head

for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node
temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)

print()
    
def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def addOne(head):
    head = reverse(head)
    temp = head
    carry = 1
    while temp:
        temp.data = temp.data + carry
        if temp.data<10:
            carry=0
            break
        else:
            temp.data=0
            carry=1
        temp=temp.next
        if carry==1:
            newhead=Node(carry)
            head=reverse(head)
            newhead.next=head
        return newhead
    head=reverse(head)    
    return   head

head=addOne(head)
temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    
    













    











