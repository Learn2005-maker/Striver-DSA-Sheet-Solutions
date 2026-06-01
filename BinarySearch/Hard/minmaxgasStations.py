# Brute Force approach
# One of the hardest problems to solve using brute force approach. We can add the gas stations one by one and calculate the maximum distance
# between two gas stations after adding each gas station. This approach will take O(k*n) time where k is the
# number of gas stations to be added and n is the number of existing gas stations.
# Time Complexity: O(k*n) where k is the number of gas stations to be added and n is the number of existing gas stations
arr = [1, 13, 17, 23]
n = len(arr)
k = 5

howMany = [0] * (n - 1)

for gasStations in range(1, k + 1):
    maxSection = float('-inf')
    maxInd = -1

    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        sectionLength = diff / (howMany[i] + 1)

        if sectionLength > maxSection:
            maxSection = sectionLength
            maxInd = i

    howMany[maxInd] += 1

maxAns = float('-inf')

for i in range(n - 1):
    diff = arr[i + 1] - arr[i]
    sectionLength = diff / (howMany[i] + 1)
    maxAns = max(maxAns, sectionLength)

print(round(maxAns, 2))


# Better Approach — Max Heap (Priority Queue)
# 🧠 Intuition (same as brute, just faster)
# You always pick the largest section
# Instead of scanning all gaps every time → use a max heap
# Heap always gives the largest section in O(log n)

# Store:
# (section_length, index)
# Each time:
# Pop largest section
# Increase station count for that gap
# Push updated section back

import heapq
arr = [1, 13, 17, 23]
n = len(arr)
k=5
howMany = [0] * (n - 1)
heap = []
# max heap (use negative values)
for i in range(n - 1):
    diff = arr[i + 1] - arr[i]
    heapq.heappush(heap, (-diff, i))
# print(heap)
for _ in range(k):
    diff,i=heapq.heappop(heap)
    diff=-diff  
    howMany[i]+=1
    newLen = (arr[i + 1] - arr[i]) / (howMany[i] + 1)
    heapq.heappush(heap, (-newLen, i))

# answer = max section
maxAns = -heap[0][0]
print(maxAns)
# Time Complexity: O(k log n) where k is the number of gas stations to be added and 
# n is the number of existing gas stations

# # Optimal Approach — Binary Search
# # 🧠 Intuition
# Instead of placing stations:
# 👉 We guess the answer
# Let:

# max distance = D
# We check:
# 👉 “Can we make all gaps ≤ D using ≤ k stations?”
# 🔍 Key Idea
# For each gap:
# stations needed = ceil(gap / D) - 1
# 🧪 Example Check

# Let’s try:
# D = 3
# Gaps:
# 12 → needs: ceil(12/3)-1 = 4-1 = 3
# 4 → ceil(4/3)-1 = 2-1 = 1
# 6 → ceil(6/3)-1 = 2-1 = 1
# Total = 5 stations ✅ (valid)

# 🔄 Binary Search Flow
# Search range:
# low = 0
# high = max gap = 12
# Keep shrinking range until precision 10^-6
# 🧪 Dry Run (short)
# mid	stations needed	valid?
# 6	2	✅
# 3	5	✅
# 2	8	❌

# 👉 Answer → around 3

# Time Complexity
# Time: O(n log range)
# Best solution 
import math
def requiredStations(arr,dist):
    count=0
    for i in range(len(arr)-1):
        gap=arr[i+1]-arr[i]
        count+=math.ceil(gap/dist)-1
    return count
arr = [1, 13, 17, 23]
k = 5
n=len(arr)
low = 0
high=max(arr[i + 1] - arr[i] for i in range(n - 1))

# precision 10^-6
while high-low>1e-6:
    mid=(low+high)//2
    if requiredStations(arr,mid)>k:
        low=mid
    else:
        ans=mid
        high=mid
print(round(ans, 6))        
