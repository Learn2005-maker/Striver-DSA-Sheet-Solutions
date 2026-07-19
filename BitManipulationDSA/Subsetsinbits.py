def subsets(nums) :
    n=len(nums)
    subsets=1<<n
    ans=[]
    for num in range(subsets):
        lis=[]
        for i in range(n):
            if num & (1<<i):
                lis.append(nums[i])
        ans.append(lis)
    return ans   

nums=[1,2,3]
res=subsets(nums)
print(res)
