def Nge(arr):
    n=len(arr)
    nge=[0]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while not stack and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            nge[i]=-1
        else:
            nge[i]=stack[-1]
        stack.append(arr[i])        
    return nge        
    
arr=[4,0,8,5,6,7]
result=Nge(arr)
print(result)
# Time complexity: O(2n)
# space complexity:O(n)+O(n)