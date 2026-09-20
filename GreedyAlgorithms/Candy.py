ratings = [1,0,2]

n=len(ratings)

left=[0]*n
right=[0]*n

left[0]=1
right[n-1]=1
for l in range(1,n): 
    if ratings[l]>ratings[l-1]:
        left[l]=left[l-1]+1
    else:
        left[l]=1

for r in range(n-2,-1,-1):
    if ratings[r]>ratings[r+1]:
        right[r]=right[r+1]+1
    else:
        right[r]=1

summ=0

for i in range(n):
    summ+=max(left[i],right[i])

print(summ)

# Time Complexity:O(2n)
ratings=[1,0,2]

n=len(ratings)

left=[0]*n
left[0]=1

for l in range(1,n): 
    if ratings[l]>ratings[l-1]:
        left[l]=left[l-1]+1
    else:
        left[l]=1
summ=max(1,left[n-1])
curr=1
for r in range(n-2,-1,-1):
    if ratings[r]>ratings[r+1]:
        curr=curr+1
    else:
        curr=1
    summ+=max(left[r],curr)
print(summ)




ratings=[1,0,2]

n=len(ratings)
summ=1
i=1
while i<n:
    if ratings[i]==ratings[i-1]:
        summ+=1
        i+=1
        continue
    peak=1
    while i<n and ratings[i]>ratings[i-1]:
        peak+=1
        summ+=peak
        i+=1
    down=1
    while i<n and ratings[i]<ratings[i-1]:
        summ+=down
        down+=1
        i+=1
    if down>peak:
        summ+=down-peak

print(summ)


# Time complexity: O(n)
# Space complxity:O(1)

