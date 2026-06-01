# Best time to buy and sell stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

prices = [7,1,5,3,6,4]
n=len(prices)
maxi=0
cost=float("-inf")
mini=prices[0]
for i in range(1,n):
    cost=prices[i]-mini
    maxi=max(maxi,cost)
    mini=min(mini,prices[i])

print(maxi ) 




# Brute Force Approach
# Time Complexity: O(n^2)
nums = [10, 7, 5, 8, 11, 9]

n=len(nums)
max_profit=0
for i in range(n):
    for j in range(i+1,n):
        max_profit=max(max_profit,nums[j]-nums[i])
    
    
print(max_profit)  