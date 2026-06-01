# Brute Force
# Time Complexity: O(m * n)
# where m and n are the number of rows and columns in the matrix respectively.


mat = [ [1, 0, 1], [0, 0, 1], [1, 1, 1] ]

max_count=-1
row_index=-1
for i in range(len(mat)):
    count_max=-1
    for j in range(len(mat[0])):
        if mat[i][j] == 1:
            count_max += 1
    if count_max > max_count:
        max_count = count_max
        row_index = i

print(row_index)



def lowerBound(nums,target):
    low=0
    high=len(nums)-1
    ans=len(nums)
    while low<= high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

m=len(mat)
n=len(mat[0])

for i in range(m):
    count_max=m-lowerBound(mat[i],1)
    if count_max > max_count:
        max_count = count_max
        row_index = i
print(row_index)    