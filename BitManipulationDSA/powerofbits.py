def myPow(x,n):
        nn=n
        ans=1.0
        if nn<0:
            nn=-1*n
        while nn>0:
            if nn&1:
                ans*=x
                nn=nn-1
            else:
                x=x*x
                nn//=2
        if n<0:
            ans=1.0/ans
        return ans           
    
 
x=2.0000
n=10    
res=myPow(x,n)

print(res)
    