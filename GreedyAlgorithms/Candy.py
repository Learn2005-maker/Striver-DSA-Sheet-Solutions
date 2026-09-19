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

