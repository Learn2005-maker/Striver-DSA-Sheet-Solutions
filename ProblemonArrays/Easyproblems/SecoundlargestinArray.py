# Function to find the second largest element
# BruteForce approach
class Solution:
    def secoundLargestElement(self,nums):
        n=len(nums)
        # Check if the array has less than 2 elements
        if n<2:
            return -1
        # Sort the list in ascending order
        nums.sort()
         # Largest element will be at last index
        Largest=nums[-1]
        s_lar=float("-inf")
        # Traverse the sorted list from right to left
        for i in range(n-2,-1,-1):
            if nums[i]!=Largest:
                s_lar=nums[i]
                break
        return s_lar
    

# Example usage
nums = [1, 2, 4, 6, 7, 5]

# Create an instance of the Solution class
sol = Solution()

''' Call the method to find 
the second largest element'''
ans = sol.secoundLargestElement(nums)

print("The second largest element is:", ans)    

# Time complexity O(nlogn) due to sorting and N is the length of the array
# Space Complexity: O(1)


# Better Approach without sorting

class Solution:

    def secondLargestElement(self, nums):
        # Get the length of the array
        n = len(nums)

        # Check if the array has less than 2 elements
        if n < 2:
            # If true, return -1 indicating there is no second largest element
            return -1 

        # Initialize variables to store the largest and second largest elements
        largest = nums[0]
        secondLargest = float('-inf')

        # First traversal to find the largest element
        for i in range(n):
            largest = max(largest, nums[i])

        # Second traversal to find second largest element
        for i in range(n):
            if nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]

        # Return the second largest element
        return -1 if secondLargest == float('-inf') else secondLargest


nums = [1, 2, 4, 6, 7, 5]

# Create an instance of the Solution class
sol = Solution()

"""Call the method to find the second 
largest element and store the result"""
result = sol.getSecondLargest(nums)

print("Second largest is", result)



# Time complexity O(n)+O(n)=O(2n) where n is the length of the array
# Space Complexity: O(1)


# Optimal Approach in single traversal

from typing import List

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return -1

        largest =  float('-inf')
        second_largest =  float('-inf')

        for num in nums:

            if num > largest:
                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:
                second_largest = num

        return -1 if second_largest == float('-inf') else second_largest

# Main function
if __name__ == "__main__":
    nums = [1, 2, 4, 6, 7, 5]

   #Creating an instance of the Solution class
    sol = Solution()

    result = sol.secondLargestElement(nums)
    print("Second largest is:", result)

# Time complexcity :O(n)
# Ṣpace complexcity: O(1)