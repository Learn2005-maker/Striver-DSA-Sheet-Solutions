# Palindrome Linked List

# BRUTE FORCE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Array
arr = [1, 2, 3, 2, 1]
pos = 1

# Convert array to linked list
head = Node(arr[0])
temp = head


for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node
    
# Time complexity: O(N)
# Space complexity: O(N)

arr=[]
temp=head
while temp:
    arr.append(temp.data)
    temp=temp.next
l=0
r=len(arr)-1
while l<=r and arr[l]==arr[r]:
    l+=1
    r-=1
print(l>r)    


# if arr==arr[::-1]:
#     print(True)
# else:
#     print(False)    


# Time complexity: O(N)
# Space complexity: O(N)   
stack=[]
temp=head
while temp:
    stack.append(temp.data)
    temp=temp.next
    
temp=head
while temp:
    if temp.data!=stack.pop():
        print(False)
        break
    temp=temp.next
else:
    print(True)             
    

# Definition for singly-linked list node
class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def is_palindrome(head):

    # Step 1: Find middle of linked list
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    # Step 2: Reverse second half
    previous_node = None
    current_node = slow_pointer

    while current_node:
        next_node = current_node.next

        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    # Step 3: Compare first half and reversed second half
    first_half = head
    second_half = previous_node

    while second_half:

        if first_half.value != second_half.value:
            return False

        first_half = first_half.next
        second_half = second_half.next

    return True



