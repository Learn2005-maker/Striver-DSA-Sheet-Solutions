sticks = [2,4,3]
n=len(sticks)

import heapq
heap=[]

total=0
for i in range(n):
    heapq.heappush(heap,sticks[i])

while len(heap)>1:
    min1=heapq.heappop(heap)
    min2=heapq.heappop(heap)
    t=min1+min2
    total+=t
    heapq.heappush(heap,t)
print(total)
# T.c:O(nlogn)
# S.c:O(n)

