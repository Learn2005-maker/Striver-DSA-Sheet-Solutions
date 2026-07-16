dividend =22
divisor = 3

# INT_MAX=2**31
# INT_MIN=2**31-1
total=0
count=0
sign=1 if divisor>0 else -1

while dividend>=abs(divisor)+total:
    count+=1
    total+=abs(divisor)
    
print(count)

# Time complexcity: O(dividend)

# Time complexcity:O(logn )^2
    
