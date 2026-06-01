class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Array
arr = [10, 20, 30, 40]
pos = 1

# Convert array to linked list
head = Node(arr[0])
temp = head

nodes = [head]

for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node
    nodes.append(new_node)

# Create cycle
temp.next = nodes[pos]

# Detect cycle
dici = {}

temp = head

while temp:

    if temp in dici:
        print("True")
        break

    dici[temp] = 1
    temp = temp.next

else:
    print("False")
    
    
    
    
# Optimal Approach
# Time complexity: O(N)
# Space complexity: O(1)
slow=fast=head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        print("Cycle detected")
        break
else:
    print("No Cycle")    