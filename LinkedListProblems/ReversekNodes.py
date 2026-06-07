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
    
arr=[1,2,3,4,5,6,7,8,9,10,11]
head=create_dll(arr)
print_forward(head)



def findK(temp,k):
    k-=1
    while temp and k>0:
        k-=1
        temp=temp.next
    return temp

def reverse(temp):
    prev=None
    while temp:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev   



def Reversenodes(head,k):
    temp=head
    prevnode=None
    while temp:
        kthNode=findK(temp,k)
        if kthNode==None:
            if prevnode:
                prevnode.next=temp
            break
        nextNode=kthNode.next
        kthNode.next=None
        newHead=reverse(temp)
        if temp==head:
            head=newHead
        else:
            prevnode.next=newHead
        prevnode=temp
        temp=nextNode
    return head
k=3    
head=Reversenodes(head,k)
print_forward(head)













