import heapq
# here - Indicates the maxHeap . beause heapq by default it is minHeap.
nums = [3,2,1,5,6,4]
k = 2

n=len(nums)
heap=[]
for i in range(n):
    if len(heap)<k:
        heapq.heappush(heap,-nums[i])
    elif nums[i]<-heap[0]:
        heapq.heapreplace(heap,-nums[i])

print(-heap[0])
