# Time complexity O(n^2)
nums=[4,2,5,1]
n=len(nums)
nge=[-1]*n
for i in range(n):
    for j in range(i+1,n):
        if nums[j]<nums[i]:
            nge[i]=nums[j]
            break
            
print(nge)

# Time complexity O(n)
nums=[4,2,5,1]
n=len(nums)
stack=[]
nge=[-1]*n
for i in range(len(nums)-1,-1,-1):
    while stack and stack[-1]>=nums[i]:
        stack.pop()
    if stack:
        nge[i]=stack[-1]
    stack.append(nums[i])
print(nge)