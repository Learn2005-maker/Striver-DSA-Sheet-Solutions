# Brute Force 
# Time complecity: O(n^2)
# Space complecity: O(n^2)
mat=[[1,2,3],[7,5,6],[4,8,9]]
r=len(mat)
c=len(mat[0])

ans=[[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        ans[j][r-1-i]=mat[i][j]
        
print(ans)

# Better Approach
# Time complecity:  ~ O(n^2)
# Space complecity: O(1)
mat=[[1,2,3],[4,5,6],[7,8,9]]

r=len(mat)
c=len(mat[0])

for i in range(r):
    for j in range(i+1,r):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        
for row in mat:
    row.reverse()
    
print (mat)