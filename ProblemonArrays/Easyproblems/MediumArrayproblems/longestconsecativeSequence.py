# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Brutre Force Approach to find longest consecutive sequence
# time complexity O(n^3)
#  space complexity O(1)   
def linearSearch(nums,x):
    for i in range(len(nums)):
        if nums[i]==x:
            return True
    return False        




nums=[102,4,100,1,101,1,101,3,2,1,1]

n=len(nums)
longest=1

for i in range(n):
    x=nums[i]
    cur_count=1
    while linearSearch(nums,x+1)==True:
        x=x+1
        cur_count+=1
    longest=max(longest,cur_count)  
    
print(longest)    
               
               
# Better Approach to find longest consecutive sequence
# time complexity O(nlogn) + O(n) due to sorting
# space complexity O(1)
nums=[102,4,100,1,101,1,101,3,2,1,1]
n=len(nums)
nums.sort()

lastSmaller=float("-inf")
longest=1
cur_count=0

for i in range(n):
    if nums[i]-1==lastSmaller:
        cur_count+=1
        lastSmaller=nums[i]
    elif nums[i]!=lastSmaller:
        cur_count=1
        lastSmaller=nums[i]
    longest=max(longest,cur_count)  
    
print(longest)    
    
    
# Optimal Approach to find longest consecutive sequence
# time complexity O(n)
# space complexity O(n) for using set data structure
# nums=[102,4,100,1,101,1,101,3,2,1,1]
nums = [0,3,7,2,5,8,4,6,0,1]
n=len(nums)
 
s=set()

for i in range(n):
    s.add(nums[i])
longest=1

for num in s:
    x=num
    if num-1 not in s:
        count=1
        x=num
        while x+1  in s:
            count+=1
            x+=1
        longest=max(longest,count)        
        
print(longest)            
        
    
        
                
    
        
                       