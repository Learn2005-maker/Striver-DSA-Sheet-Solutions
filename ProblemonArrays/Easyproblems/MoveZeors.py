# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]




# Using an Extra Array (Easier to Understand)

nums = [0,1,0,3,12]
n=len(nums)
arr=[]
for i in range(n):
    if nums[i]!=0:
        arr.append(nums[i])

zeros=[0]*(len(nums)-len(arr))


print(arr+zeros)

# Simple two pointer Approach...
# When we find the non-zero elemnt swap both if them.
nums=[0,1,0,3,12]

j=0
n=len(nums)
for i in range(n):
    if nums[i]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
        
print(nums)        
    