# iven an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.
# Example 1
# Input : nums = [4, 2, 2, 6, 4], k = 6
# Output : 4

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
nums = [4, 2, 2, 6, 4]
k = 6
n=len(nums)


count=0
for i in range(n):
    xor=0
    for j in range(i,n):
        xor^=nums[j]
        
        if xor==k:
            count+=1
print(count)     



# Better Approach using HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

nums = [4, 2, 2, 6, 4]
k = 6
n=len(nums)


count=0
dici={}
xor=0
for i in range(n):
    xor=xor^nums[i]
    
    if xor==k:
        count+=1
    required =xor^k
    
    if required in dici:
        count+=dici[required]
    dici[xor]=dici.get(xor,0)+1
print(count)    
        
