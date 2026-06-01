# Brute Force Way  (only poistives)
class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums) 
        maxLength = 0

        # starting index
        for startIndex in range(n):
            # ending index
            for endIndex in range(startIndex, n):
                # add all the elements of 
                # subarray = nums[startIndex...endIndex]
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)




# Optimal Way using sliding window
nums = [10, 5, 2, 7, 1, 9]
k=15
# nums = [-3, 2, 1]
# k=6
n=len(nums)

cur_sum=0
l=0
max_len=0
for r in range(n):
    if nums[r]<=0:
        cur_sum=0
# You reset the sum because the current subarray becomes invalid.
# Everything before this index is useless for further windows.
        l=r+1
# You move the left pointer to the element after the invalid one.
        continue  
    cur_sum+=nums[r]
    
    while cur_sum>k and l<=r:
        cur_sum-=nums[l]
        l+=1
    max_len=max(max_len,r-l+1)

print(max_len)    
        
 
        
# Better Approach using HashMap (works for negative numbers + positives)
# Tc: O(n)
# Sc: O(n)
class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)  

        preSumMap = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            # calculate the prefix sum till index i
            sum += nums[i]

            # if the sum equals k, update maxLen
            if sum == k:
                maxLen = max(maxLen, i + 1)

            # calculate the sum of remaining part i.e., sum - k
            rem = sum - k

            # calculate the length and update maxLen
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)

            # update the map if sum is not already present
            if sum not in preSumMap:
                preSumMap[sum] = i

        return maxLen

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)
 