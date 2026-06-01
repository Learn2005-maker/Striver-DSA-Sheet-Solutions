def binarySearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        
        if target==nums[mid]:
            return mid
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
            
    return ans
nums = [1,2,2,2,2,2,4,5]
target = 2

print(binarySearch(nums,target))  

 

