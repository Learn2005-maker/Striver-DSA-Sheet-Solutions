
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
    
    