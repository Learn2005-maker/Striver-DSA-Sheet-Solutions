nums=[4,5,6,7,0,1,2]
n=len(nums)
target=1
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(mid)
        break
    # Left Half
    if nums[low]<=nums[mid]:
        if nums[low]<=target and target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
    # Checking at rigth half 
    else:
        if nums[mid]<=target and target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
else:
    print(-1)        
# Time complexcity: O(log n)
# Space complexcity: O(1)


# Sorted and Rotaed Array with Duplicates | Leetcode 81

nums=[1,0,1,1,1]
target = 0
n=len(nums)
low=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]==target:
        print(True)
        break
    # Handling Duplicates
    if nums[low]==nums[mid]==nums[high]:
        low+=1
        high-=1
    # Left Half
    elif nums[low]<=nums[mid]:
        if nums[low]<=target<=nums[mid]:
            high=mid-1
        else:
            low=mid+1
    # Checking at rigth half 
    else:
        if nums[mid]<=target and target<=nums[high]:
            low=mid+1
        else:
            high=mid-1
else:
    print(False)  
    
