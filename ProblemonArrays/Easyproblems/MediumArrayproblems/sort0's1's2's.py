
# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
# The sorting must be done in-place, without making a copy of the original array.

# In brute force approach we can use inbuilt sort function to sort the array. or we can apply merge sort or quick sort to sort the array.
# But in optimal approach we can use Dutch National Flag Algorithm to sort the array in a single pass.


nums=[0,1,2,0,1,2,0,0,1,2,0]
n=len(nums)

low=0
mid=0
high=n-1

while mid<=high:
    if nums[mid]==0:
        nums[mid],nums[low]=nums[low],nums[mid]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    else:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1
        
print(nums)        

# Time Complexity:
# O(n) — single pass through the list.
# O(1) — constant extra space.


# better approach
nums=[0,1,2,0,1,2,0,0,1,2,0]
count0=0
count1=0
count2=0

for i in range(n):
    if nums[i]==0:
        count0+=1
    elif nums[i]==1:
        count1+=1
    else:
        count2+=1

for i in range(count0):
    nums[i]=0
for i in range(count0,count0+count1):
    nums[i]=1
for i in range(count0+count1,n):
    nums[i]=2
print(nums)
# Time Complexity:
# O(n) + O(n)— single pass through the list.
# O(1) — constant extra space. 
