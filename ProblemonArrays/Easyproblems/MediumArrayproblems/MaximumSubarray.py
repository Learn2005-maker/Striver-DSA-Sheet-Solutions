# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.


# Brute Force Approach to find Maximum Subarray Sum
# time complexity O(n^3)

arr = [2, 3, 5, -2, 7, -4]
n=len(arr)

ans=float("-inf")
for i in range(n):
    temp=0
    for j in range(i,n):
        temp+=arr[j]   
        for k in range(i,j+1):
            temp+=arr[k]
        ans=max(ans,temp)

print(ans)
# Better Approach to find Maximum Subarray Sum
# time complexity O(n^2)

# Initialize the maximum sum to a very small value
arr = [2, 3, 5, -2, 7, -4]
n = len(arr)
max_sum = float("-inf")

# Iterate through all possible subarrays
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr[j]
        max_sum = max(max_sum, current_sum)

print(max_sum)




# Kadena's Algorithm to find Maximum Subarray Sum
# Time complexity O(n)
arr = [2, 3, 5, -2, 7, -4]
n = len(arr)
add=0
maxi=float("-inf")
start=-1
end=-1
startindex=0
for i in range(n):
    if add==0:
        startindex=i
    add+=arr[i]
    if add>maxi:
        maxi=add
        start=startindex
        end=i
    if add<0:
        add=0
# If you want to return the subarray itself, you can keep track of the start and end indices.
subarray = arr[start+1:end+1]
print(subarray)
print(maxi)
# Time Complexity: O(n)
