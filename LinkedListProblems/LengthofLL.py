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
dici={}


count=0
temp=head
while temp:
    if temp in dici:
        print(count-dici[temp])
        break
    dici[temp]=1
    count+=1
    temp=temp.next
else:
    print(0)

# Time complexity: O(N)
# Space complexity: O(N)


 
def findLength(fast,slow)  :  
    temp=slow.next
    count=1
    
    while temp!=slow:
        count+=1
        temp=temp.next
    return count        
   

s=f=head
while f and f.next:
    s=s.next
    f=f.next.next
    if s==f: 
        print(findLength(s,f))
        break
else:
    print(0)
# Time complexity: O(N)
# Space complexity: O(1)