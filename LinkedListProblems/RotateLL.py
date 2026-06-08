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
    
arr=[1,2,3,4,5,6]
head=create_dll(arr)
print_forward(head)



def findNthNode(temp,k):
    while temp and k>1:
        k-=1
        temp=temp.next
    return temp    


def rotateLL(head,k):
    if head is None or k==0:
        return head
    length=1
    tail=head
    while tail.next:
        length+=1
        tail=tail.next
    
    if k%length==0:
        return head
    k=k%length    
    tail.next=head
    newTailNode=findNthNode(head,length-k)
    newhead=newTailNode.next
    newTailNode.next=None
    return newhead
k=2    
head=rotateLL(head,k)    
print_forward(head)





