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
    
arr=[1,2,3,1,4]
head=create_dll(arr)
print_forward(head)



def deleteOccurence(head,target):
    temp=head
    while temp:
        nextNode=temp.next
        prevNode=temp.prev
        if temp.data==target:
            if temp==head:
                head=head.next
            if nextNode:
                nextNode.prev=prevNode   
            if prevNode:
                prevNode.next=nextNode
            temp=temp.next
        else:
            temp=temp.next
    return head
target=1
head=deleteOccurence(head,target)
print_forward(head)









