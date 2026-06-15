# Brute force approach
# Time complexity O(n) and space complexity O(1)
x=2.00000
n=-3

ans=1
for i in range(abs(n)):
    ans*=x
if n<0:
    ans=1/ans
print(ans)    


# Using Built in function
x=2.00000
n=-3
print(pow(x,n))

# Binary Exponentiation
# Time Complexcity:O(logn) and SC:(1)
def myPower(x,n):
    nn=n
    ans=1.0
    if nn==0:
        return 1
    if nn<0:
        nn=n*-1
    while nn>0:
        if nn%2==0:
            x=x*x
            nn=nn/2
        else:
            ans=ans*x
            nn=nn-1
    if n<0:
        ans=1.0/ans
    return ans 
x=2.0000
n=10
res=myPower(x,n)
print(res)
        
def power(x, n):
    if n == 0:
        return 1
    if n<0:
        return 1/power(x, -n)
    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


print(power(2, 10))  # 1024    

# Time Complexcity:O(logn) and SC:(logn) 