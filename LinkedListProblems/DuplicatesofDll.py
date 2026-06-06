class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
# Create DLL from array
def create_dll(arr):

    # Empty array
    if len(arr) == 0:
        return None

    # Create head node
    head = Node(arr[0])

    temp = head

    # Create remaining nodes
    for i in range(1, len(arr)):

        new_node = Node(arr[i])

        temp.next = new_node
        new_node.prev = temp
        temp = new_node

    return head


# Print DLL forward
def print_forward(head):

    temp = head

    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next

    print("None")
    
arr=[1,1,1,1,2,3,3,4,4,4,4,4]
head=create_dll(arr)
print_forward(head)

def removeDuplicates(head):
    temp=head
    while temp and temp.next:
        if temp.data==temp.next.data:
            duplicate=temp.next
            temp.next=duplicate.next
            if duplicate.next:
                duplicate.next.prev=temp
        else:
            temp=temp.next
    return head    
    
head= removeDuplicates(head)
print_forward(head)
    
# print(head)