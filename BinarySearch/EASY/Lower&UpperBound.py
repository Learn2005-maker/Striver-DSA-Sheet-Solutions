
# Upper Bound and Lower Bound
def lowerBound(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else: 
            low = mid + 1
            
    return ans


nums = [1,2,2,2,3,4]
print(lowerBound(nums,2))


def upperBound(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans


nums = [1,2,2,2,3,4]
print(upperBound(nums,2))