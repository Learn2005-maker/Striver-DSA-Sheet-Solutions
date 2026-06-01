# Medium problem

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Optimal appraoch without  using Extra  space
# right rotation of array by k times is equivalent to
# 1. reverse the whole array
# 2. reverse first k elements
# 3. reverse last n-k elements

# But for left rotation of array by k times is equivalent to
# 1. reverse the first k elements
# 2. reverse the last n-k elements
# 3. reverse the whole array

def reverse(i,j):
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
        

nums=[-1,-100,3,99]
k=2
n=len(nums)
k=k%n  # it handles k>n 
i=0
j=n-1

reverse(i,j)  # reverse th whole array
reverse(i,k-1) # rev first k elements
reverse(k,n-1) # reverse last elements
print(nums)



# Using Extra space

nums = [-1,-100,3,99]
k = 2
n=len(nums)

n1=nums[n-k:]
n2=nums[:n-k]

n3=n1+n2

print(n3)

# Brute force approach
#  right Rotate the array by one step k times  

nums=[2,1,3,4]
n=len(nums)

temp=nums[n-1]

for i in range(n-1,-1,-1):
    nums[i]=nums[i-1]
nums[0]=temp

print(nums)


# left Rotate the array by one step k times

nums=[2,1,3,4]
n=len(nums)

temp=nums[0]

for i in range(n-1):
    nums[i]=nums[i+1]
nums[n-1]=temp

print(nums)
