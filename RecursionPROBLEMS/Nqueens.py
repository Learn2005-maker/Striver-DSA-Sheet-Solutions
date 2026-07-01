def isSafe(row,col,board,n):
    # upper left diagoanl
    r,c=row,col
    while r>=0 and c>=0:
        if board[r][c]=='Q':
            return False
        r-=1
        c-=1
    #left side
    r,c=row,col
    while c>=0:
        if board[r][c]=='Q':
            return False
        c-=1
    # lower left diagonal
    r,c=row,col
    while r<n and c>=0:
        if board[r][c]=='Q':
            return False
        r+=1
        c-=1
    return True
def solve(col,board,ans,n):
    if col==n:
        ans.append([''.join(row) for row in board])
        return
    for row in range(n):
        if isSafe(row,col,board,n):
            board[row][col]='Q'
            solve(col+1,board,ans,n)
            board[row][col]='.'
def nQueens(n):
    board=[['.' for _ in range(n)]for _ in range(n)]
    # board=[['.']*n]*n
    ans=[]
    solve(0,board,ans,n)
    return ans
n=4
print(nQueens(n))