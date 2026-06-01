
# Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2
nums = [1, 3, 5, 6]
target = 2
n=len(nums)

l=0
h=n-1
ans=n
while l<=h:
    mid=(l+h)//2
    if nums[mid]>=target:
        ans=mid
        h=mid-1
    else:
        l=mid+1
print(ans)        