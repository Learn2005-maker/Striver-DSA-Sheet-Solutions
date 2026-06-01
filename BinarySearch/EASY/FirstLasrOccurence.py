       
# For finding first and last occurence # 
count=0        
def searchRange(nums, target):
    # Find First Occurrence
    low = 0
    high = len(nums) - 1
    first = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            first = mid
            high = mid - 1   # move left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # Find Last Occurrence
    low = 0
    high = len(nums) - 1
    last = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            last = mid
            low = mid + 1    # move right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    

# CountOccurences = last - first + 1
    if first != -1 and last != -1:
        count=last-first+1
    else:
        count=0    
    return [first, last,count]    
nums = [1,2,2,2,3,4]
target = 2

print(searchRange(nums, target))    

