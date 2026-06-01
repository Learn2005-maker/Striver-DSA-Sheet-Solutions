nums = [1, -2, 3, 5, 7, 9]
target = 7


n=len(nums)
temp=[]
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            for d in range(c+1,n):
                if nums[a]+nums[b]+nums[c]+nums[d]==target:
                    quadruplets=tuple(sorted([nums[a],nums[b],nums[c],nums[d]]))
                    temp.append(quadruplets)
                    
res=[list(i) for i in temp]
print(res)


# Better Approach
nums = [1, -2, 3, 5, 7, 9]
target = 7

n=len(nums)
uniq=set()
for a in range(n):
    for b in range(a+1,n):
        seen=set()
        for c in range(b+1,n):
            fourth=target-(nums[a]+nums[b]+nums[c])
            if fourth in seen:
                quadriplet=tuple(sorted([nums[a],nums[b],nums[c],fourth]))
                uniq.add(quadriplet)
            seen.add(nums[c])   
            
res=[list(i) for i in  uniq]

print(res)



# Optimal Approach

nums = [1, -2, 3, 5, 7, 9]
target = 7
n=len(nums)
nums.sort()

res=[]
for a in range(n):
    if a>0 and nums[a]==nums[a-1]:
        continue
    for b in range(a+1,n):
        if b>a+1 and nums[b]==nums[b-1]:
            continue
        c=b+1
        d=n-1
        while c <d:
            quadralet=nums[a]+nums[b]+nums[c]+nums[d]
            
            if quadralet<target:
                c+=1
            elif quadralet>target:
                d-=1
            else:
                res.append([nums[a],nums[b],nums[c],nums[d]])
                c+=1
                d-=1
                while c<d and nums[c]==nums[c-1]:
                    c+=1
                while c<d and nums[d]==nums[d+1]:
                    d-=1
                
print(res)   
# Complexity

# Sorting → O(N log N)

# 2 loops + 2 pointer → O(N³)

# Space → O(1) (excluding answer)