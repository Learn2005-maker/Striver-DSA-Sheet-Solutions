

def dfs(i,j,grid):
    if i<0 or j<0 or i>=n or j>=m or grid[i][j]=='0':
        return

    grid[i][j]='0'

    dfs(i+1,j,grid)
    dfs(i,j+1,grid)
    dfs(i-1,j,grid)
    dfs(i,j-1,grid)





grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]




n=len(grid)
m=len(grid[0])
count=0
for i in range(n):
    for j in range(m):
        if grid[i][j]=='1':
            dfs(i,j,grid)
            count+=1    

print(count)
