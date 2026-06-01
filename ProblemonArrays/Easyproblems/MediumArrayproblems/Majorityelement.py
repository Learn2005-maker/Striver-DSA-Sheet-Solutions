# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Brute Force Approach
# time complexity O(n^2)
def majorityElement(nums):
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        if count > n // 2:
            return nums[i]
    return -1

nums = [3, 2, 3]
print(majorityElement(nums))



# Better approach using HashMap
# time complexity O(n)

n=len(nums)

dici={}
ans=0
for i in range(n):
    ch=nums[i]
    if ch not in dici:
        dici[ch]=1
    else:
        dici[ch]+=1

for i,j in dici.items():
    if j>n//2:
        ans=i
print(ans)
# Optimal Approach using Boyer-Moore Voting Algorithm
# time complexity O(n)

# You can find the majority element in O(n) time and O(1) space using the Boyer–Moore Voting Algorithm:
nums=[2,2,1,1,2,2]
# nums=[1,2,3,4,5,6]
el=0
count=0
n=len(nums)//2
for num in nums:
    if count==0:
        el=num
    # count+=(1 if el==num else -1)    
        count=1
    elif num==el:
        count+=1
    else:
        count-=1
if nums.count(el)> n:
    print(el)
else:
    print(-1)