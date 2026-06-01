nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
n = len(nums)

found = False

if n == 1:
    print(nums[0])

for i in range(n):
    if i == 0:
        if nums[i] != nums[i+1]:
            print(nums[i])
            found = True
            break
    elif i == n-1:
        if nums[i] != nums[i-1]:
            print(nums[i])
            found = True
            break
    else:
        if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
            print(nums[i])
            found = True
            break

if not found:
    print(-1)
    
    
    
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
n = len(nums)

found = False

if n == 1:
    print(nums[0])

elif nums[0] != nums[1]:
    print(nums[0])

elif nums[n-1] != nums[n-2]:
    print(nums[n-1])

else:
    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            print(nums[mid])
            found = True
            break

        if (mid % 2 == 1 and nums[mid-1] == nums[mid]) or (mid % 2 == 0 and nums[mid+1] == nums[mid]):
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print(-1)
        
#  Using binary search       # 
# Time complexity: O(log n)
# space complexity: O(1)
nums=[1,5,1,2,1]
n=len(nums)

if n==1:
    print(0)
elif nums[0]>nums[1]:
    print(0)
elif nums[n-1]>nums[n-2]:
    print(n-1)
else:
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            print(mid)
            break
        if nums[mid]>nums[mid-1]:
            low=mid+1
        # elif nums[mid]>nums[mid+1]:
        #     high=mid-1
        else:
            low=mid+1
            # Or high=mid+1
                