# Given a binary array nums, return the maximum number of consecutive 1s in the array.

# A binary array is an array that contains only 0s and 1s.


# Example 1

# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

# Output: 3

# Explanation:

# The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s
nums = [1, 1, 1,1,1, 1, 1, 0]

n=len(nums)
count=0
max_count=0
for i in range(n):
    if nums[i]==1:
        count+=1
        
        if count>max_count:
            max_count=count
    else:
        count=0

print(max_count)        
