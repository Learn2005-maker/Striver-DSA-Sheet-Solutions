def splitArray(nums,split):
    subarrays=1
    length=0
    for num in nums:
        if length+num>split:
            subarrays+=1
            length=num
        else:
            length+=num
    return subarrays

nums = [7,2,5,10,8]
k = 2

low=max(nums)
high=sum(nums)

while low<=high:
    mid=(low+high)//2
    if splitArray(nums,mid)<=k:
        high=mid-1
    else:
        low=mid+1
print(low)        
# Time Complexity
# Binary Search: O(log(sum - max))