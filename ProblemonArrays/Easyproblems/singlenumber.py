# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Find the number that appears once, and other numbers twice.
# brute force approach
nums=[1,1,2,4,4]
n=len(nums)


for i in range(n):
    num=nums[i]
    count=0
    for j in range(n):
        if nums[j]==num:
            count+=1
            
    if count==1:
        print(num)

# optimal way
nums=[1,1,2,4,4]
n=len(nums)      
xor=0
for i in range(n):
    xor^=nums[i]
    
print(xor)    
