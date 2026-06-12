
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        dici={None:None}
        # dici[None]=None
        while temp:
            newnode=Node(temp.val)
            dici[temp]=newnode
            temp=temp.next
        temp=head
        while temp:
            copynode=dici[temp]  
            copynode.next=dici[temp.next]
            copynode.random=dici[temp.random]
            temp=temp.next 
        return dici[head]
    

# Optimized approach without using extra space
# time complexity O(3n) and space complexity O(1) without the result linked list space

def copyNodesinBetween(head):
    temp=head
    while temp:
        newnode=Node(temp.val)
        newnode.next=temp.next
        temp.next=newnode
        temp=temp.next.next
def connectRandompointers(head):
    temp=head
    while temp:
        copynode=temp.next
        if temp.random:
            copynode.random=temp.random.next
        else:
            copynode.random=None
        temp=temp.next.next
        
def newCopyLinkedList(head):
    temp=head
    dummynode=Node(-1)
    res=dummynode
    while temp:
        # copynode=temp.next
        res.next=temp.next
        res=res.next
        temp.next=temp.next.next
        temp=temp.next
    return dummynode.next    
    
def copyLinkedList(head):
    copyNodesinBetween(head)
    connectRandompointers(head)
    newHead=newCopyLinkedList(head)
    return newHead
    