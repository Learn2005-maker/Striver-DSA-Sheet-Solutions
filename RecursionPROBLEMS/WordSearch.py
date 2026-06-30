def exist(board,word):
    rows=len(board)
    cols=len(board[0])
    
    def dfs(i,j,index):
        if len(word)==index:
            return True
        if i<0 or j<0 or i>=rows or j>=cols:
            return False
        if board[i][j]!=word[index]:
            return False
        found=(
            dfs(i+1,j,index+1) or
            dfs(i-1,j,index+1) or
            dfs(i,j+1,index+1) or 
            dfs(i,j-1,index+1)
        )
        return found
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False            
  
    

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
ans=exist(board,word)    
print(ans)