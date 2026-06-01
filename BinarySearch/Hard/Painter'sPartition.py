def isPaintpossible(A,C,maxTime):
    paintBoard=0
    painter=1
    for num in C:
        if paintBoard+num>maxTime:
            painter=painter+1
            paintBoard=num
        else:
            paintBoard+=num
    return painter <=A    
A=2
B=5
C=[10,20,30,40]
low=max(C)
high=sum(C)

while low<=high:
    mid=(low+high)//2
    if isPaintpossible(A,C,mid):
        high=mid-1
    else:
        low=mid+1
print(low)        
print(low*B)   # If they ask in Time

# Complexity
# Binary Search: O(log(sum - max))