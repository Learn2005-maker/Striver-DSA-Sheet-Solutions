
# Time complexity:O(n-k)*O(k) ans S.C :O(n-k++)
nums=[1,3,-1,-3,5,3,6,7]
k=3
ans=[]
for i in range(len(nums)-k+1):
    maxi=nums[i]
    for j in range(i,i+k):
        maxi=max(maxi,nums[j])
    ans.append(maxi)

print(ans)        



from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

dq = deque()
lis = []

for i in range(len(nums)):

    # Remove elements outside the current window
    if dq and dq[0] <= i - k:
        dq.popleft()

    # Remove smaller elements from the back
    while dq and nums[dq[-1]] <= nums[i]:
        dq.pop()

    # Add current index
    dq.append(i)

    # Start adding answers when window size becomes k
    if i >= k - 1:
        lis.append(nums[dq[0]])

print(lis)