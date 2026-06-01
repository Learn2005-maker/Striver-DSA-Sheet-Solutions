# Brute Force Solution

nums = [1, 1, 1]

k = 2
n = len(nums)

count = 0

for i in range(n):
    cur_sum = 0
    for j in range(i, n):
        cur_sum += nums[j]
        if cur_sum == k:
            count += 1

print(count)



# Optimal Solution

nums = [1, 1, 1]
k = 2

prefix=0
count=0
dici={0:1}  # Base case: there's one way to have a prefix sum of 0 (by taking no elements)
for num in nums:
    prefix+=num
    rem= prefix-k   
    if rem in dici:
        count+=dici[rem]
    # dici[prefix]=dici.get(prefix,0)+1
    if prefix in dici:
        dici[prefix]+=1
    else:
        dici[prefix]=1
print(count) 
print(dici)