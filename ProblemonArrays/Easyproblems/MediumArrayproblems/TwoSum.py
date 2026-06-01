# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Brute force way to solve Two Sum Problem
# time complexity O(n^2)

nums=[2,7,11,15]
target=9
n=len(nums)
flag=False
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            flag=True

if flag:
    print("Found")
else:
    print("not Found")
    
# optimal way to solve Two Sum Problem by using HashMap
# time complexity O(n) 

arr=[2,7,11,15]
target=9
n=len(arr)

dici={}

for i,num in enumerate(arr):
    diff =target-num
    if diff in dici:
        print(dici[diff],i)
        print("True")
        break
    dici[num]=i    
else:
    print("False")

# optimal way to solve Two Sum Problem by using Two Pointer Approach
# time complexity O(nlogn) due to sorting
arr=[2,7,6,8,11]
target=9
n=len(arr)
arr.sort()
l=0
r=n-1


while l<r:
    total=arr[l]+arr[r]
    if total==target:
        print("Yes")
        break
    elif total>target:
        r-=1
    else:
        l+=1
else:        
    print("False")        
        


