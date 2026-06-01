# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.
# Return the length of such a subarray. If no such subarray exists, return 0.
# Example 1
# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation:

# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.
# Brute Force Approach
# Time complexity: O(n^2)
nums = [15, -2, 2, -8, 1, 7, 10, 23]

n=len(nums)
max_len=0
 
for i in range(n):
    cur_sum=0
    for j in range(i,n):
        cur_sum+=nums[j]
        if cur_sum==0:
            max_len=max(max_len,j-i+1) 
print(max_len)            
 
# Better Approach using HashMap (works for negative numbers + positives)
# Time Complexity: O(n)
# Space Complexity: O(n)
dici={}
pre_sum=0
maxlen=0
for i in range(n):
    pre_sum+=nums[i]
    
    if pre_sum==0:
        maxlen=max(maxlen,i+1)
    
    if pre_sum in dici:
        length=i-dici[pre_sum]
        maxlen=max(maxlen,length)
    else:
        dici[pre_sum]=i
print(maxlen)    
        