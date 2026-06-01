# Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1
# Input: nums = [4, 5, 3, 7, 1, 2]
# Output: 840
# Explanation:
# The largest product is given by the whole array itself
# Brute force approach: O(n^2)
# nums = [-5, 0, -2]
nums=[2,3,-2,4]
n=len(nums)

max_pro=nums[0]
for i in range(n):
    cur_product=1
    for j in range(i,n):
        cur_product*=nums[j]
        
        max_pro=max(max_pro,cur_product)
print(max_pro)


max_pro=nums[0]
min_pro=nums[0]
result=nums[0]
for i in range(1,n):
    cur=nums[i]
    
    temp_max=max(cur,cur*max_pro,cur*min_pro)
    temp_min=min(cur,cur*min_pro,max_pro*cur)
    max_pro=temp_max
    min_pro=temp_min
    result=max(result,max_pro)
print(result)


# Key Insight to Remember
# 👉 In product problems:
# Always track both max and min, because negative numbers flip the sign.

nums=[2,4,-1,-5,3]
n=len(nums)

prefix=1
suffix=1
result=float("-inf")

for i in range(n):
    if prefix==0:
        prefix=1
    if suffix==0:
        suffix=1 
    prefix*=nums[i]
    suffix*=nums[n-1-i]
    result=max(result,max(prefix,suffix))
print(result)    