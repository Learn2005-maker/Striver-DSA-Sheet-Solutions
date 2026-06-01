# Find the minimum element in a rotated sorted array
nums=[4,5,6,7,0,1,2]
n=len(nums)
low=0
high=n-1
mini=float("inf")
while low<=high:
    mid=(low+high)//2
    # If Array is already sorted
    if nums[low]<=nums[high]:
        mini=min(mini,nums[low])
        break
    if nums[low]<=nums[mid]:
        mini=min(nums[low],mini)
        low=mid+1
    else:
        mini=min(nums[mid],mini)
        high=mid-1
print(mini)


# Find out how many times the array is rotated
# Another approach to find the minimum element in a rotated sorted array
# This approach also keeps track of the index of the minimum element found so far.
# 
nums=[4,5,0,1,2]

n=len(nums)
low=0
high=n-1
mini=float("inf")
index=-1

while low<=high:
    mid=(low+high)//2

    # If array already sorted
    if nums[low]<=nums[high]:
        if nums[low] < mini:
            mini=nums[low]
            index=low
        break

    # Left half sorted
    if nums[low]<=nums[mid]:
        if nums[low] < mini:
            mini=nums[low]
            index=low
        low=mid+1

    # Right half sorted
    else:
        if nums[mid] < mini:
            mini=nums[mid]
            index=mid
        high=mid-1

print(mini)
print(index)
