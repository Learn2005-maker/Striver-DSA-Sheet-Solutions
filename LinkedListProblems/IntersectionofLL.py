# Approach 1: Using a Set
# Intuition
# Store all values from the first list in a set.
# Traverse the second list.
# If a value exists in the set, it is common.
    
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

# A: 3 -> 1 -> 4 \
#                 6 -> 2
# B: 1 -> 2 -> 4 -> 5 /


# Time Complexity: O(n+m) and Space Complexity: O(n) where n and m are the lengths of the two linked lists.
s = set()

temp = headA
while temp:
    s.add(temp.data)
    temp = temp.next

temp = headB    

while temp:
    if temp.data in s:
        print(temp.data, end=" ")
    temp = temp.next
    
# Time Complexity: O(n+m) and Space Complexity: O(n) where n and m are the lengths of the two linked lists. 
def getIntersectionNode(headA, headB):

    p1 = headA
    p2 = headB

    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1
intersection = getIntersectionNode(headA, headB)

print()
print()
if intersection:
    print(intersection.data)
else:
    print("No intersection")

# temp = headA
# while temp.data != 6:
#     temp = temp.next

# intersection = temp
# print(intersection.data)