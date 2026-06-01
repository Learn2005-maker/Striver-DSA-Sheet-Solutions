def isAllocationPossible(nums,book):
    pages=0
    student=1
    for num in nums:
        if pages+num>book:
            student=student+1
            pages=num
        else:
            pages+=num
    return student        
        
nums = [25, 46, 28, 49, 24]
m=4


for book in range(max(nums),sum(nums)):
    if isAllocationPossible(nums,book)<=m:
        print(book)
        break


# Complexity
# Binary Search: O(log(sum - max))
# Each check: O(n)
# ✅ Total: O(n log(sum))
def isAllocationPossible(nums,book):
    pages=0
    student=1
    for num in nums:
        if pages+num>book:
            student=student+1
            pages=num
        else:
            pages+=num
    return student        
        
nums = [25, 46, 28]
m=4
if m>len(nums):
    print(-1)
else:
    low=max(nums)
    high=sum(nums)
    while low<=high:
        mid=(low+high)//2
        if isAllocationPossible(nums,mid)<=m    :
            high=mid-1
        else:
            low=mid+1
    print(low)      