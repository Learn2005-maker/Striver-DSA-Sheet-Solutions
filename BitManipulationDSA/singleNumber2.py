# Time complexcity:O(n)
# space complexcity:O(n)
# Single number 2 Problem..
nums=[1,1,1,2,3,3,3]

n=len(nums)
dici={}

for i in range(n):
    dici[nums[i]]=dici.get(nums[i],0)+1

for i in dici:
    if dici[i]==1:
        print(i)

# Using bit manipulation 
#  Time complexcity:O(n*32) 
# space complexcity:O(1)
nums = [0,1,0,1,0,1,99]
ans=0
for bit in range(31):
    count=0
    for i in range(len(nums)):
        if nums[i] & (1<<bit):
            count+=1
    if count%3==1:
        ans=ans | (1<<bit)
print(ans)        
        

# This is sorting approach  Time complexicity:O(nlogn)
nums=[3,2,2,2]
nums.sort()
n=len(nums)
for i in range(1,n,3):
    if nums[i]!=nums[i-1]:
        print(nums[i-1])
print(nums[n-1])        

# time complexcity:O(n)
nums=[5,5,6,7,7,7,5]
n=len(nums)
ones=0
twos=0
for i in nums:
    ones=ones ^ i & (~twos)
    twos=twos ^ i & (~ones)
print(ones)
        

