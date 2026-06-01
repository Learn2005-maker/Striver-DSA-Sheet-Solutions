

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [10, 20, 30, 40]

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

# Length
count = 0
temp = head

while temp:
    count += 1
    temp = temp.next

print("Length:", count)

# Search
key = 30
temp = head

found = False

while temp:
    if temp.data == key:
        found = True
        break
    temp = temp.next

if found:
    print("Element Found")
else:
    print("Element Not Found")