nums = [1,1,1,2,2,3]
k = 2
n=len(nums)

mpp={}
for num in nums:
    mpp[num]=mpp.get(num,0)+1
lis=list(mpp)
lis.sort(key= lambda x : (-mpp[x],x))

ans=lis[:k]
print(ans)


# Time complexity: O ( n log u)

import heapq
nums = [1,1,1,2,2,3]
k = 2
mpp={}
for i in nums:
    mpp[i]=mpp.get(i,0)+1
heap=[]
for i in mpp:
    heapq.heappush(heap,(mpp[i],i))
    if len(heap)>k:
        heapq.heappop(heap)

ans=[]
for freq,i in heap:
    ans.append(i)
print(ans)

