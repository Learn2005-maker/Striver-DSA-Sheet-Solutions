
# Time complexcity:O(max(n*log(max(nums))))

from math import ceil
def isdivisor(nums,limit,div):
    total=0
    for num in nums:
        total+=ceil(num/div)
        #total += (num + div - 1) // div
    return total<=limit
        
nums=[1,2,3,4,5]
limit=8

for div in range(1,max(nums)):
    if isdivisor(nums,limit,div):
        ans=div
        break
print(ans)



# Time complexcity:O(nlogn)
from math import ceil
def isdivisor(nums,limit,div):
    total=0
    for num in nums:
        total+=ceil(num/div)
        #total += (num + div - 1) // div
    return total<=limit
        
nums=[1,2,3,4,5]
limit=8
low=min(nums)
high=max(nums)

while low<=high:
    mid=(low+high)//2
    if isdivisor(nums,limit,mid):
        high=mid-1
    else:
        low=mid+1


print(low)