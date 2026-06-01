# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
# Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.




arr=[3,4,5,1,2]

n=len(arr)
count=0
for i in range(n):
    if arr[i]>arr[(i+1)%n]:
        count+=1




if count<=1:
    print("True")
else:
    print("False")
    print("The array is not sorted.")
    
    
    
    
#Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
# This is Strivers Question .
class Solution:
    def isSorted(self, nums):
        #your code goes here
        isSorted=True
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                isSorted=False
                break
        return isSorted

        
# For decending Just opposite logic nums[i]>nums[i-1] 
#  time complexcity: O(n)
# Space complexcity: O(1)

    