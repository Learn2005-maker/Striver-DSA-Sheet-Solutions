def isValid(board,row,col,ch):
    for i in range(9):
        if board[row][i]==ch:
            return False
        if board[i][col]==ch:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==ch:
            return False
    return True        
    
def solve(board):
    n=len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]==".":
                for num in range(1,10):
                    ch=str(num)
                    if isValid(board,i,j,ch):
                        board[i][j]=ch
                        if solve(board)==True:
                            return True
                        else:
                            board[i][j]="."   
                return False    
    return True  
    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solve(board)


print(board)

for row in board:
    print(row)
    
# time complexity: O(9^(n*n)) where n is the size of the board (9 in this case). 
# space complexity: O(n*n) for the recursion stack and the board itself.
