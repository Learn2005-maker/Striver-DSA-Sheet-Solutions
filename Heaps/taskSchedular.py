import heapq
from collections  import deque
tasks = ["A","A","A","B","B","B"]
n = 2
freq={}
for task in tasks:
    freq[task]=freq.get(task,0)+1
heap=[]


for task,count in freq.items():
    heapq.heappush(heap,(-count,task))
q=deque()

# (Remaining_count,avaliable_time)
time=0
while heap or q:
    time+=1
    # move cooled-down tasks back to heap
    if q and q[0][1]==time:
        count,task=q.popleft()
        heapq.heappush(heap,(count,task))
    if heap:
        count,task=heapq.heappop(heap)
        count+=1
        if count!=0:
            q.append((count,time+n+1))
print(time)




