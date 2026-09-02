nums = [1,1,1,2,2,3]
k = 2
n=len(nums)

mpp={}
for num in nums:
    mpp[num]=mpp.get(num,0)+1
lis=list(mpp)
lis.sort(key= lambda x : (-mpp[x],x))

ans=lis[:k]
print(ans)
