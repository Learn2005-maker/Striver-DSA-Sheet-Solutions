def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    
    return merge(left,right)
    
def merge(left,right):
    array=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            array.append(left[i])
            i+=1
        else:
            array.append(right[j])
            j+=1
    array.extend(left[i:])
    array.extend(right[j:])
    return array
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [3,9,4,8]

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

arr=[]
temp=head
while temp:
    arr.append(temp.data)
    temp=temp.next
print(arr)    

result=merge_sort(arr)  
print(result)

temp=head
i=0
while temp:
    temp.data=result[i]
    print(temp.data,end=" -> ")
    i+=1
    temp=temp.next
print(None)    
# Time complexity: O(n log n) and space complexity: O(n)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [3,9,4,8]

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



def findMiddle(head):
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow


    

def merge(firstHalf, secoundHalf):
    t1=firstHalf
    t2=secoundHalf
    dummyNode=Node(-1)
    temp=dummyNode
    while t1 and t2:
        if t1.data<=t2.data:
            temp.next=t1
            temp=temp.next
            t1=t1.next
        else:
            temp.next=t2
            temp=temp.next
            t2=t2.next
    if t1:
        temp.next=t1
    else:
        temp.next=t2
    return dummyNode.next    



def merge_sort(head):
    if head is None or head.next is None:
        return head
    mid=findMiddle(head)
    firstHalf=head
    secoundHalf=mid.next
    mid.next=None
    firstHalf=merge_sort(firstHalf)
    secoundHalf=merge_sort(secoundHalf)
    return merge(firstHalf, secoundHalf)


head=merge_sort(head)

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    
            
            
# Time  : O(n log n)
# Space : O(log n)   # recursion stack        
    