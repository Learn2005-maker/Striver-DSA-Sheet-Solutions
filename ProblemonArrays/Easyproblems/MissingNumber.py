# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


from typing import List

class Solution:
    # Function to find the missing number
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate N from the length of nums
        N = len(nums) 
        
        # Outer loop that runs from 0 to N
        for i in range(0, N+1):
            """ Flag variable to check 
            if an element exists"""
            flag = 0
            
            """ Search for the element
            using linear search"""
            for num in nums:
                if num == i:
                    # i is present in the array
                    flag = 1
                    break
            
            """ Check if the element 
            is missing (flag == 0)"""
            if flag == 0:
                return i
        
        """ The following line will never 
        execute, it is just to avoid warnings"""
        return -1

# Main function to test the implementation
if __name__ == "__main__":
    nums = [0,1, 2, 4]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the missingNumber method to find the missing number
    ans = solution.missingNumber(nums)
    
    print(f"The missing number is: {ans}")








nums=[3,0,1]

n=len(nums)
mis=0
for i in range(n+1):
    if i not in nums:
        mis=i
print(mis)
# optimal approach using sum of n formula
# time complexity O(n)
nums=[1,2,4,5]
n=len(nums)+1

sum_of_n=n*(n+1)//2

sum_of_nums=sum(nums)
missing_number=sum_of_n - sum_of_nums

print(missing_number)

# optimal approach using XOR
# time complexity O(2n)
nums=[1,2,4,5]
n=len(nums)

xor_n=0
xor_nums=0
for i in range(1,n+1):
    xor_n^=i
for num in nums:
    xor_nums^=num
        
missing_number=xor_n^xor_nums

print(missing_number)

# we can decrese to O(2n) to O(n) time complexity by doing both xor in single loop


nums=[1,2,4,5]
n=len(nums)+1

xor=0
xor_nums=0

for i in range(n-1):
    xor_nums^=nums[i]
    xor^=i+1
    xor1=xor^n

missing_number=xor1^xor_nums
print(missing_number)
