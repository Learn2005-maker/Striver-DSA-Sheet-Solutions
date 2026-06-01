# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]


# Brute Force
# Time Complexcity:  O(n^3)
# Space Complexcity: O(1)


def Row(rows):
    for j in range(cols):
        if nums[i][j]!=0:
            nums[i][j]=-1

def Column(cols):
    for i in range(rows):
        if nums[i][j]!=0:
            nums[i][j]=-1


# nums = [[1,1,1],[1,0,1],[1,1,1]]
nums=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

rows=len(nums)
cols=len(nums[0])
for i in range(rows):
    for j in range(cols):
        if nums[i][j]==0:
            Row(i)
            Column(j)

for i in range(rows):
    for j in  range(cols):
        if nums[i][j]==-1:
            nums[i][j]=0
            
print(nums)       



#  Better Approach
# Time Complexcity:  O(n^2)
# Space Complexcity: O(m+n)  

nums=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

rows=len(nums)
cols=len(nums[0])
r_size=[0]*rows
c_size=[0]*cols
for i in range(rows):
    for j in range(cols):
        if nums[i][j]==0:
            r_size[i]=1
            c_size[j]=1
            
for i in range(rows):
    for j in range(cols):
        if r_size[i]!=0 or c_size[j]!=0:
            nums[i][j]=0

print(nums)            
            

# Optimal Approach

matrix = [[1,1,1],[1,0,1,],[1,1,1]]

r=len(matrix)
c=len(matrix[0])
col0=1

for i in range(r):
    for j in range(c):
        if matrix[i][j]==0:
            # mark the i-th row -->  column
            matrix[i][0]=0
            # mark the j-th column --> row
            if j!=0:
                matrix[0][j]=0
            else:
                col0=0
                
for i in range(1,r):
    for j in range(1,c):
        if matrix[0][j]==0 or matrix[i][0]==0:
            matrix[i][j]=0
# marking i - th row
if matrix[0][0]==0:
    for j in range(c):
        matrix[0][j]=0
# marking j  -  th column

if col0==0:
    for i in range(r):
        matrix[i][0]=0
            
print(matrix)            
            
        
            
            
 