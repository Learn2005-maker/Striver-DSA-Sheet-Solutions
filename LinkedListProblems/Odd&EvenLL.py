# Time complexity: O(N)
# Space complexity: O(N)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Array
arr = [1,2,3,4,5,6]

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
while temp and temp.next:
    arr.append(temp.data)
    temp=temp.next.next
if temp:    
    arr.append(temp.data)
    
temp=head.next
while temp and temp.next:
    arr.append(temp.data)
    temp=temp.next.next
if temp:
    arr.append(temp.data)    
print(arr)    

temp=head
i=0
while temp:
    temp.data=arr[i]
    print(temp.data,end=" -> ")
    i+=1
    temp=temp.next
print(None)    







class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head

sol=Solution()
head=sol.oddEvenList(head)
# Time complexity: O(N)
# Space complexity: O(1)    