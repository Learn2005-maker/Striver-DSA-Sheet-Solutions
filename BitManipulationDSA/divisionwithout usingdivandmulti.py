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
def fns(dividend,divisor):
    ans=0
    INT_MAX=2**31-1
    INT_MIN=-2**31
     # Overflow case
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    sign= -1 if (dividend<0) ^ (divisor<0) else 1   
    # Work with positive values
    n = abs(dividend)
    d = abs(divisor)
    if n>=0 and d<0:
        sign=False
    if n<=0 and d>0:
        sign=False
    while n>=d:
        count=0
        while n>=(d<<(count+1)):
            count+=1
        ans+=(1<<count)
        n-=(d<<count)
    return ans if sign==1 else -ans       

dividend =22
divisor = 3

res=fns(dividend,divisor)
print(res)


    
