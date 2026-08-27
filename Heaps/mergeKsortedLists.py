class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

import heapq

heap=[]
for i,node in enumerate(lists):
    if node:
        heapq.heappush(heap,(node.val,i,node))
dummy=ListNode(0)
tail=dummy
while heap:
    value,i,node=heapq.heappop(heap)
    tail.next=node
    tail=tail.next
    if node.next:
        heapq.heappush(heap,(node.next.val,i,node.next))


print(dummy.next)
# T.c:O(nlog k) and S.c is :O(k)
