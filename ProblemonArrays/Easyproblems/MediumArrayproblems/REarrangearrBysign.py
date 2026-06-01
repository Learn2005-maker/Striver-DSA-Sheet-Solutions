# Brute Force Approach to rearrange array by sign
# Time complexity O(n)+O(n/2)
# space complexity O(n)
arr = [3, 1, -2, -5, 2, -4]
n = len(arr)

pos = []
neg = []

# Step 1: Separate positives and negatives
for i in range(n):
    if arr[i] > 0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])

# Step 2: Place them alternately back into arr
n1 = len(pos)
for i in range(n1):
    arr[2 * i] = pos[i]
    arr[2 * i + 1] = neg[i]

print(arr)

# Optimal Approach to rearrange array by sign
# Time complexity O(n)
# space complexity O(n)
arr=[3,1,-2,-5,2,-4]
n=len(arr)
ans=[0]*n
posindex=0

negindex=1
for i in range(n):
    if arr[i]<0:
        ans[negindex]=arr[i]
        negindex+=2
    else:
        ans[posindex]=arr[i]
        posindex+=2
        
print(ans)


# Rerranging array by sign  instead pos >neg or neg > pos
# Time complexity O(2n)
# space complexity O(n)
nums = [2, 4, 5, -1, -3, -4,5,6,-4,2,-9,-4,-6]

n=len(nums)

pos=[]
neg=[]

for i in range(n):
    if nums[i]>0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])
n1=len(pos)
n2=len(neg)  

if n1>n2:
    for i in range(n2):
        nums[2*i]=pos[i]
        nums[2*i+1]=neg[i]
    index=2*n2    
    for i in range(n2,n1):
        nums[index]=pos[i]
        index+=1
else:
    for i in range(n1):
        nums[2*i]=pos[i]
        nums[2*i+1]=neg[i]
    index=2*n1    
    for i in range(n1,n2):
        nums[index]=neg[i]
        index+=1
    
print(nums)
