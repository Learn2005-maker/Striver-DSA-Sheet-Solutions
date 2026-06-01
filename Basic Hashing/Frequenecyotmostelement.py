# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums 
# and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.


nums=[1,2,4]
k=5
nums.sort()
l=0
n=len(nums)
temp=0
ans=0
for r in range(n):
    temp+=nums[r]
    
    while nums[r]*(r-l+1)-temp >k:
        temp-=nums[l]
        l+=1
    
    ans=max(ans,r-l+1)
print(ans)    


