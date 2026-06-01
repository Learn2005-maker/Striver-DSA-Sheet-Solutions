import math

num = 25
sqrt_num = math.sqrt(num)

print("Square root:", sqrt_num)


# Using linear search Time complexcity:O(n) space complexity:O(1)
n=25
ans=1
for i in range(1,n):
    if i*i<=n:
        ans=i
    else:
        break
print(ans) 


# Using Binary search Time complexcity:O(log n)
# space complexity:O(1)
low=1
high=n
ans=1
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(ans)  
# ans or high 
print(high)


