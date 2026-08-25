# Celebrity Problem
# Time complexity:O(n*m)+O(n)
def celebrity(matrix):
    n=len(matrix)
    m=len(matrix[0])
    knowMe=[0]*m
    iKnow=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                knowMe[j]+=1
                iKnow[i]+=1 
    for i in range(n):
        if knowMe[i]==n-1 and iKnow[i]==0:
            return i
    return -1                     

matrix=[[0,1,1,0],
        [0,0,0,0],
        [0,1,0,0],
        [1,1,0,0]]    
res=celebrity(matrix)
print(res) 


# Celebrity Problem
# Time complcity:O(n) and S.c:O(1)
def celebrity(matrix):
    n=len(matrix)
    m=len(matrix[0])
    top=0
    down=n-1
    while top<down:
        if matrix[top][down]==1:
            top+=1
        elif matrix[down][top]==1:
            down-=1
        else:
            top+=1
            down-=1
    if top>down:
        return -1
    # Verify the candidate
    if top==down:
        if all(matrix[top][i] == 0 and matrix[i][top] == 1 for i in range(n) if i != top):
            return top
    return -1  
      
matrix=[
        [0,1,1,0],
        [0,0,0,0],
        [0,1,0,0],
        [1,1,0,0]
        ]    
res=celebrity(matrix)
print(res) 
