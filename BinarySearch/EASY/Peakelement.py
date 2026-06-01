nums = [1, 2, 3, 4, 5, 6, 7, 8,5,1]
n = len(nums)
found = False

for i in range(n):
    
    # first element
    if i == 0:
        if nums[i] > nums[i+1]:
            print(i)
            found = True
            break
    
    # last element
    elif i == n-1:
        if nums[i] > nums[i-1]:
            print(i)
            found = True
            break
    
    # middle elements
    elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        print(i)
        found = True
        break

if not found:
    print(-1)
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    
# using binary search
def findPeakElement(nums):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > nums[mid + 1]:
            high = mid-1
        else:
            low = mid + 1
            
    return low 


print(findPeakElement(nums))
# Time complexity: O(log n)