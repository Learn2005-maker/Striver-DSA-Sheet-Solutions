# Brute` Force Approach
# Time complexity: O(nlogn)+`O(n*maxDist)` where maxDist is the maximum distance between the first and last stall

class Solution:
    # Function to check if cows can be placed with min distance d
    def canPlace(self, stalls, cows, d):
        # Place the first cow at the first stall
        count = 1
        lastPos = stalls[0]

        # Try placing remaining cows
        for i in range(1, len(stalls)):
            # If current stall is at least 'd' away from last cow
            if stalls[i] - lastPos >= d:
                # Place a cow here
                count += 1
                lastPos = stalls[i]
            # If all cows placed successfully
            if count >= cows:
                return True
        # Not possible to place all cows
        return False

    # Function to find maximum minimum distance using brute force
    def aggressiveCows(self, stalls, cows):
        # Step 1: Sort stall positions
        stalls.sort()

        # Step 2: Get the maximum possible distance
        maxDist = stalls[-1] - stalls[0]

        # Step 3: Variable to store answer
        ans = 0

        # Step 4: Try all possible distances from 1 to maxDist
        for d in range(1, maxDist + 1):
            # If cows can be placed with distance d
            if self.canPlace(stalls, cows, d):
                # Update answer
                ans = d

        # Step 5: Return the maximum valid distance
        return ans


# Driver code
stalls = [1, 2, 8, 4, 9]
cows = 3
obj = Solution()
print(obj.aggressiveCows(stalls, cows))




# Optimlized Approach
# Time complexity: O(nlogn) + O(log(maxDist)*n) where maxDist is
def canWePlace(nums, cows, dist):
    countCows = 1
    lastPos = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - lastPos >= dist:
            countCows += 1
            lastPos = nums[i]

    return countCows >= cows


nums = [0,3,4,7,10,9]
cows = 4

nums.sort()

low = 1
high = nums[-1] - nums[0]
ans = 0

while low <= high:
    mid = (low + high) // 2

    if canWePlace(nums, cows, mid):
        ans = mid
        low = mid + 1   # try bigger distance
    else:
        high = mid - 1

print(ans)
