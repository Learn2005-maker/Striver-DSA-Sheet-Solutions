# nums = [3, 5, 4, 1, 1]
# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
# Note: You are not allowed to modify the original array.
# Ths=is is my bri=ute force Approavh with time complexity O(n^2) and space complexity O(1)
nums = [1, 2, 3, 6, 7, 5, 7]
n=len(nums)

result=[]
for i in range(n):
    for j in range(i+1,n):
        if nums[i]==nums[j]:
            result.append(nums[j])
            break
for i in range(1,n+1):
    if i not in nums:
        result.append(i)
    
print(result)   

# Time complexity: O(n^2) due to the nested loops. We can optimize it to O(n) using a hash set to track seen numbers and identify the duplicate
# and missing values in a single pass.
nums = [1, 2, 3, 6, 7, 5, 7]
n=len(nums)


rep=0
mis=0
for i in range(1,n+1):
    count=0
    for j in nums:
        if i==j:
            count+=1
    if count==2:
        rep=i
    elif count==0:
        mis=i
print([rep,mis])

# Time complexity: O(n^2) due to the nested loops. We can optimize it to O(n) using a hash set to track seen numbers and identify the duplicate
# and missing values in a single pass.

# Optimal approach using Hashing: O(n) for counting O(n) for checking time and O(n) space
nums = [1, 2, 3, 6, 7, 5, 7]
n=len(nums)

dici={}

for i in range(n):
    x=nums[i]
    if x not in dici:
        dici[x]=1
    else:
        dici[x]+=1
rep=-1
mis=-1
for i in range(1,n+1):
    if i  not in dici:
        mis=i
    elif dici[x]==2:
        rep=i
        
print([rep,mis])      


# Time complexity: O(n) and Space complexity: O(1)
nums=[1,2,3,6,7,5,7]

n=len(nums)

# Step 1: Difference of sums
expected_sum = n*(n+1)//2
actual_sum = sum(nums)
val1 = actual_sum - expected_sum   # R - M

# Step 2: Difference of squares
expected_sq_sum = n*(n+1)*(2*n+1)//6
actual_sq_sum = sum(x*x for x in nums)
val2 = actual_sq_sum - expected_sq_sum   # R² - M²

# Step 3: Solve equations
R_plus_M = val2 // val1

R = (val1 + R_plus_M) // 2
M = R - val1

print("Repeating:", R)
print("Missing:", M)


# Optimal approach using Bit Manipulation: O(n) time and O(1) space
nums=[1,2,3,6,7,5,7]

n=len(nums)

xor=0
for i in range(n):
    xor^=nums[i]
for i in range(1,n+1):
    xor^=i

set_bit=xor & -xor
x=0 # This refers to 0th Bit   
y=0 # This refers to 1th Bit   
for num in nums:
    if num & set_bit :
        x^=num
    else:
        y^=num
for i in range(1,n+1):
    if i & set_bit :
        x^=i
    else:
        y^=i
if nums.count(x)==2:
    rep=x
    mis=y
else:
    rep=y
    mis=x
    
print([rep,mis])    
    
    

    

  
    
    