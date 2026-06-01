nums=[10,22,3,1,12,9]
n=len(nums)
ans=[]
for i in range(n):
    flag=True
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            flag=False
            break
    if flag==True:
        ans.append(nums[i])
print(ans)            


nums=[10,22,3,1,12,9]
n=len(nums)
ans=[]
maxi=float("-inf")
for i in range(n-1,-1,-1):
    if nums[i]>maxi:
        ans.append(nums[i])
        # maxi=nums[i]
    maxi=max(maxi,nums[i])    
ans.reverse()    
print(ans)    
# Time Complexity: O(n)   
