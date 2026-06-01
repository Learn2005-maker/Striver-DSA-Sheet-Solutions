
# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


#Optimal solution
arr=[1,1,2,2,2,3,3]
n=len(arr)
i=0
for j in range(1,n):
    if arr[j]!=arr[i]:
        arr[i+1]=arr[j]
        i+=1
print(i+1)  #to increse index from 2 to 3
print(arr[:i+1])#modified arry
   
# 2nd way
# Using set()

arr=[1,1,1,2,2,2,3,3]  
# ans=0
# print(list(set(arr)))

sett=set()
ans=0
for i in range(len(arr)-1):
    if arr[i] not in sett:
        sett.add(arr[i])
        ans+=1
print(ans)   

print(sett)    