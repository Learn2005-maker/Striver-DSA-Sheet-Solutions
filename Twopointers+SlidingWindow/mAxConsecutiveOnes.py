nums = [1,1,1,0,0,0,1,1,1,1,0]
k=2
n=len(nums)
maxlen=0
for i in  range(n):
    zeors=0
    for j in range(i ,n):
        if nums[j]==0:
            zeors+=1
        if  zeors<=k:
            maxlen=max(maxlen,j-i+1)
        else:
            break    
print(maxlen)            
# T.C:O(n^2) and S.c:O(1)


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
n = len(nums)
max_len = 0
r = 0
l = 0
zeros = 0 
while r < n: 
    if nums[r] == 0:
        zeros += 1
        
    while zeros > k:
        if nums[l] == 0:
            zeros -= 1
        l += 1 #

    if zeros <= k:    
        max_len = max(max_len, r - l + 1)   
    r += 1
print(max_len)
# T.c:O(n+n)



# Optimization.
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
n = len(nums)
max_len = 0
r = 0
l = 0
zeros = 0 
while r < n: 
    if nums[r] == 0:
        zeros += 1
        
    if zeros > k:
        if nums[l] == 0:
            zeros -= 1
        l += 1 #

    if zeros <= k:    
        max_len = max(max_len, r - l + 1)   
    r += 1
print(max_len)