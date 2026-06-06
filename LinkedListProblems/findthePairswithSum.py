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
    
arr=[1,2,3,4,5,6,7,8,9]
head=create_dll(arr)
print_forward(head)

def findPairswithGivenSum(head,target):
    temp1=head
    arr=[]
    while temp1:
        temp2=temp1.next
        while temp2 and temp1.data+temp2.data<=target:
            if temp1.data+temp2.data==target:
                arr.append([temp1.data,temp2.data])
            temp2=temp2.next
        temp1=temp1.next
    return arr
target=5    
head=findPairswithGivenSum(head,target)

print(head)
# Time Complexity = O(n²)
# Space Complexity = O(1) excluding the output



def findTail(head):
    temp=head
    while temp.next:
        temp=temp.next
    return temp
def findPairswithGivenSum(head,target):
    left=head
    right=findTail(head)
    arr=[]
    while left.data < right.data:
        if left.data+right.data==target:
            arr.append([left.data,right.data])
            left=left.next
            right=right.prev
        elif left.data+right.data>target:
            right=right.prev
        else:
            left=left.next
    return arr
target=5    
head=findPairswithGivenSum(head,target)

print(head)
# Time Complexity = O(n)
# Space Complexity = O(1) excluding the output        