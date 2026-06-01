# Brute Force Approach
# Time Complexity: O(n)

nums=[2,3,4,7,11]

n=len(nums)
k=5
for i in range(n):
    if nums[i]<=k:
       k+=1
    else:
        break
print(k)    
       
       
# Time complexity: O(logn) using Binary Search
nums=[2,3,4,7,11]
n=len(nums)
k=5
low=0 
high=n-1
while low<=high:
    mid=(low+high)//2
    missing=nums[mid]-(mid+1)
    if missing<k:
        low=mid+1
    else:
        high=mid-1
# Formula is used Here Do (K-missing)
moreWeWant=k- (nums[high]-(high+1) )     
print(nums[high]+moreWeWant) 
print(high+k+1)
print(low+k)

# Return any one gives Same answer Only
        
           