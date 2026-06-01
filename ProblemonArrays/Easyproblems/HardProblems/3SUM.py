nums = [-1,0,1,2,-1,-4]
n=len(nums)
# i!=j ,k  and j!=k
# j>i and k>j
uniq=set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i]+nums[j]+nums[k]==0:
                # set can store only hashable thing
                triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                uniq.add(triplet)
        
res=[list(i) for i in uniq]
print(res)
 
# Better Approach 

nums = [-1,0,1,2,-1,-4]

n=len(nums)

uniq=set()
thirdK=0
for i in range(n):
    seen=set()
    for j in range(i+1,n):
        thirdK=-(nums[i]+nums[j])
        if thirdK in seen:
            triplet=tuple(sorted([nums[i],nums[j],thirdK]))
            uniq.add(triplet)
        seen.add(nums[j])    
    
res=[list(_) for _ in uniq]

print(res)
            
# Optimal Approach


nums = [-1,0,1,2,-1,-4]
n=len(nums)

nums.sort()
ans=[]
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        total=nums[i]+nums[j]+nums[k]
        
        if total < 0:
            j+=1
        elif  total >0:
            k-=1
        else:
            ans.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1
                
print(ans)                
        
        
        
     