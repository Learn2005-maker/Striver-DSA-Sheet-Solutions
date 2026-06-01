# Time Complexity: O(n+n) and Space Complexity: O(1)
class Node:
    def __init__(self, val, next=None, prev=None):
        self.data = val
        self.next = None


arr = [1, 2, 3, 4, 5,6]
# create head
head = Node(arr[0])

temp = head

# create remaining nodes
for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node


# print linked list
temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# count nodes
count = 0
temp = head

while temp:
    count += 1
    temp = temp.next
# move to middle
middle = count // 2

temp = head
for i in range(middle):
    temp = temp.next
while temp:
    print( temp.data,end=" -> ")
    temp=temp.next
    
print("None")  

def middleNode( head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
middleNode(head)
mid = middleNode(head)

while mid:
    print(mid.data, end=" -> ")
    mid = mid.next

print("None")

# Optimal code  pseudo code
# Time complexity O(n) and space complexity O(1)
if head and head.next is None:
    print(None)
slow = head
fast = head
prev=None
while fast and fast.next:
    prev=slow
    slow = slow.next
    fast = fast.next.next
prev.next=slow.next

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print(None)    

  