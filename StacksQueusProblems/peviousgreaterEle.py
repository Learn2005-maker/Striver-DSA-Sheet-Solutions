nums=[5,7,9,10,3,4]
n=len(nums)
stack=[]
nge=[-1]*n
for  i in range(n):
    while stack and stack[-1]>=nums[i]:
        stack.pop()
    if stack:
        nge[i]=stack[-1]
    stack.append(nums[i])
print(nge) 
