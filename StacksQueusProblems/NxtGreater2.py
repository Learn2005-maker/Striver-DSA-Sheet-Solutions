# Brute Force Approach
# Time Complexity: O(n^2)
# space Complexity: O(n)
arr = [1, 2, 1]
n = len(arr)
nge = [-1] * n

for i in range(n):
    # Change the upper bound from i+n-1 to i+n
    for j in range(1, n):
        ind = (i+j )% n  # circular indexing
        if arr[ind] > arr[i]:
            nge[i] = arr[ind]
            break

print(nge)


# time complexity:O(4n)  we can tell explicitly that the time complexity is O(n) 
# because each element is pushed and popped from the stack at most once.
# spac e complexity: O(n)
arr=[10,12,-1,11,12]
n=len(arr)
nge=[0]*n
stack=[]
for i in range(2*n-1 ,-1,-1):
    idx=i%n
    while stack and stack[-1]<=arr[idx]:
        stack.pop()
    
    if i<n:
        nge[i]=stack[-1] if stack else -1
    stack.append(arr[idx])    
        
print(nge)        