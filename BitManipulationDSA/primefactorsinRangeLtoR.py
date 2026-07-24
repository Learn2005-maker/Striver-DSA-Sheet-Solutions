queries = [ [2, 5], [4, 7] ]
# count prime in the range L-R:
ans=[]
n=len(queries)

for i in range(n):
    l,r=queries[i]
    lis=[]
    for num in range(l,r+1):
        Prime=True
        if num<2:
            Prime=False
        # else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                Prime=False
                break
        if Prime:
            lis.append(num)
            # count+=1
    ans.append(lis) 
print(ans)    

# Sieve erathothams 
def sieve(n):
    if n<=2:
        return 0
    # assume all the numbers are prime
    prime=[True]*(n)
    # 0 and 1 are not prime
    prime[0]=False
    prime[1]=False
    i=2 #traverse till sqrt(n)
    while i*i<=n:
        # mark all the multiples of i as non-prime
        if prime[i]:
            for j in range(i*i,n,i):
                prime[j]=False
        i+=1
    #print all the primes
    for i in range(2,n):
        if prime[i]:
            print(i,end=" , ")

n=2
sieve(n)

# time complexcity:O(N*log(logn))
# space complexcity:O(n)
        
        
    