
def Lhistrogram(arr):
    max_area=0
    stack=[]
    n=len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            element=stack[-1]
            stack.pop()
            nse=i
            pse=stack[-1] if stack else -1
            max_area=max(max_area,arr[element]*(nse-pse-1))
        stack.append(i)
    while stack:
        element=stack[-1]
        stack.pop()
        nse=n
        pse=stack[-1] if stack else -1 
        max_area=max(max_area,arr[element]*(nse-pse-1))
    return max_area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
if not matrix:
    print("0")
else:    
    n=len(matrix)
    m=len(matrix[0])
    maxArea=0
    # FIX: Use a 1D array to keep track of column heights as we go down row by row
    heights = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='1':
                heights[j]+=1
            else:
                heights[j]=0    
        maxArea=max(maxArea,Lhistrogram(heights))
print(maxArea)


