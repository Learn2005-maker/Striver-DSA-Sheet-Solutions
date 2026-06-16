mod = 10**9 + 7

def power(x,n):
    if n==0:
        return 1
    half=power(x,n//2)    
    if n%2==0:
        return (half*half)%mod
    return (x*half*half)%mod

n=5
even=(n+1)//2
odd=n//2
ans=power(5,even)*power(4,odd)
ans=ans%mod
print(ans)



