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
# Time Complexity: O(n+m) and Space Complexity: O(n) where n and m are the lengths of the two linked lists.
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


temp1=headA
temp2=headB
n1=0
n2=0
while temp1:
    n1+=1
    temp1=temp1.next
    
while temp2:
    n2+=1
    temp2=temp2.next

def collisionPoint(t1,t2,d):
    while d:
        d-=1
        t2=t2.next
    while t1!=t2:
        t1=t1.next
        t2=t2.next
    return t1    

if n1<n2:
    print(collisionPoint(headA,headB,n2-n1).data)
else:
    collisionPoint(headB,headA,n1-n2)
    
#Time Complexity: O(n1+2n2) and Space Complexity: O(1) where n and m are the lengths of the two linked lists. 

# Optimal Approach: Time Complexity: O(n1+n2) and Space Complexity: O(1) where n and m are the lengths of the two linked lists.
t1=headA
t2=headB
while t1!=t2:
    t1=t1.next if t1 else headB
    t2=t2.next if t2 else headA
    if t1==t2:
        print(t1.data)
        break
    













    


