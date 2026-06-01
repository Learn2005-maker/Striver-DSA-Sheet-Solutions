def findFloor(nums, x):
    
    n=len(nums)
    l=0
    h=n-1
    ans=-1
    
    while l<=h:
        mid=(l+h)//2
        
        if nums[mid] <= x:
            ans = nums[mid]
            l = mid + 1
        else:
            h = mid - 1
            
    return ans

def findCeil(nums, x):
    
    n=len(nums)
    l=0
    h=n-1
    ans=-1
    
    while l<=h:
        mid=(l+h)//2
        
        if nums[mid] >= x:
            ans = nums[mid]
            h = mid - 1
        else:
            l = mid + 1
            
    return ans

nums =[3, 4, 4, 7, 8, 10]
x=5

floor = findFloor(nums,x)
ceil = findCeil(nums,x)

print(floor)
print(ceil)

#Once you master Lower Bound, you solve many problems instantly.

# | Problem                | Pattern     |
# | ---------------------- | ----------- |
# | Search Insert Position | Lower Bound |
# | First Occurrence       | Lower Bound |
# | Ceil                   | Lower Bound |
