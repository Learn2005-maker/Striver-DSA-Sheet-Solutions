class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = None


arr = [1, 2, 3, 4, 5]
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
if middle==0:
    print(head.next)
for i in range(middle-1):
    temp = temp.next
temp.next=temp.next.next    
while temp:
    print( temp.data,end=" -> ")
    temp=temp.next
    
print("None")  
# Time complexity ~=O(2n) and space complexity O(1)