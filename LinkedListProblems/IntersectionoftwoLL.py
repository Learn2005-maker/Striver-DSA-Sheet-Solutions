class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
     
headA = Node(3)
headA.next = Node(1)
headA.next.next = Node(4)
headA.next.next.next = Node(6)
headA.next.next.next.next = Node(2)
# Store the node containing 6 in a variable
intersection = headA.next.next.next

headB = Node(1)
headB.next = Node(2)
headB.next.next = Node(4)
headB.next.next.next = Node(5)

headB.next.next.next.next = intersection

dici={}
temp1=headA
temp2=headB
 
while temp1:
    dici[temp1]=1
    temp1=temp1.next
while temp2:
    if temp2 in dici:
        print(temp2.data)
        break
    dici[temp2]=1
    temp2=temp2.next
else:
    print(None)
    
    


