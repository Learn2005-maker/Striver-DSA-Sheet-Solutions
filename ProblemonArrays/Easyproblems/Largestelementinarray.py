# BruteForce approach
# Given an array of integers nums, return the value of the largest element in the array

#Approach
#sort the array in ascending order and return the last element at the index of the array.

class Solution:
    def largestElement(self,nums):
        
        nums.sort()
        
        largest=nums[-1]
        
        return largest
        
if __name__=="__main__":
    nums=[2,9,-8,10,78,3,9]
    
    sol=Solution()
    Largest=sol.largestElement(nums) 
    
    print(Largest)
 # Time complexity O(nlogn) due to sorting
 # Space complexity O(1) 

# Largest element in the array in Optimal way
class Solution:
    def largestElement(self,nums):
        
        maxi=float("-inf")
        for num in nums:
            if num>maxi:
                maxi=num
        
        return maxi    
        
if __name__=="__main__":
    nums=[2,9,-8,10,78,3,9]
    
    sol=Solution()
    print(sol.largestElement(nums)) 
    # Time complexity O(n)
    # Space complexity O(1)