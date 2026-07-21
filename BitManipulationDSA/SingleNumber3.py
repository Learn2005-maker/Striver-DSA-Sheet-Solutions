# Usng dici approach
nums = [1,2,1,3,2,5]
n=len(nums)
dici={}
for i in nums:
    dici[i]=dici.get(i,0)+1
print(dici)    
ans=[]
for i in dici:
    if dici[i]==1:
        ans.append(i)
        
print(ans)        

# Time comoplexcity:O(n)
# space complexcity:O(1)
nums = [1,2,1,3,2,5]

xor = 0
for num in nums:
    xor ^= num

rightmost = xor & (-xor)

b1 = 0
b2 = 0

for num in nums:
    if num & rightmost:
        b1 ^= num
    else:
        b2 ^= num

print([b1, b2])