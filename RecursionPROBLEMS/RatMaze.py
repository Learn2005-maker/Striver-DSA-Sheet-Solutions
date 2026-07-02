def solve(i,j,grid,n,ans,move,visited):
    if i==n-1 and j==n-1:
        ans.append(move)
        return
    # downward
    if i+1<n and  not visited[i+1][j] and grid[i+1][j]==1:
        visited[i][j]=1
        solve(i+1,j,grid,n,ans,move+'D',visited)
        visited[i][j]=0
    # leftward
    if j-1>=0 and not visited[i][j-1] and grid[i][j-1]==1:
        visited[i][j]=1
        solve(i,j-1,grid,n,ans,move+'L',visited)
        visited[i][j]=0
    # RightWard
    if j+1<n and not visited[i][j+1] and grid[i][j+1]==1:
        visited[i][j]=1
        solve(i,j+1,grid,n,ans,move+'R',visited)
        visited[i][j]=0
    # Upward
    if i-1>=0 and not visited[i-1][j] and grid[i-1][j]==1:
        visited[i][j]=1
        solve(i-1,j,grid,n,ans,move+'U',visited)
        visited[i][j]=0

n=4
visited=[[0  for _ in range(n)]for _ in range(n)]

grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
ans=[]
if grid[0][0]==1:
    solve(0,0,grid,n,ans,"",visited)
print(ans)   





# Time complexity: O(4^(n^2))  because in worst case we can go in 4 direction from each cell and there are n^2 cells
# space complexity: O(n^2)  for visited array and recursion stack space
def solve(i,j,grid,n,ans,move,visited,di,dj):
    if i==n-1 and j==n-1:
        ans.append(move)
        return 
    res_str="DRLU"
    for idx in range(4):
        nexti=i+di[idx]
        nextj=j+dj[idx]
        if nexti<n and nextj<n and nexti>=0 and nextj>=0 and not visited[nexti][nextj] and grid[nexti][nextj]==1:
            visited[i][j]=1
            solve(nexti,nextj,grid,n,ans,move+res_str[idx],visited,di,dj)
            visited[i][j]=0

def findPath(grid,n):
    ans=[]
    visited=[[0  for _ in range(n)]for _ in range(n)]
    di=[1,0,0,-1]
    dj=[0,1,-1,0]
    if grid[0][0]==1:
        solve(0,0,grid,n,ans,"",visited,di,dj)
    return ans    
grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
n=4
print(findPath(grid,n))