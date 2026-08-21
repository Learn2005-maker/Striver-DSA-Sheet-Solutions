nums = [1,0,1,0,1]
goal = 2
n=len(nums)
count=0
dici={0:1}
prefixSum=0
for i in range(n):
    prefixSum+=nums[i]
    remove=prefixSum-goal
    count+=dici.get(remove,0)
    dici[prefixSum]=dici.get(prefixSum,0)+1
print(count)         
# Prefix sum based problem 
  
# T.c: O(n+n) ans S.c:O(1)
def binarySubarray(nums,goal):
    n=len(nums)
    count=0
    l=0
    r=0
    summ=0
    if goal==0:
        return 0
    while r<n:
        summ+=nums[r]
        while summ>goal:
            summ-=nums[l]
            l+=1
        count+=(r-l+1)
        r+=1
    return count

nums = [1,0,1,0,1]
goal = 2
print(binarySubarray(nums,goal)-binarySubarray(nums,goal-1))  
        