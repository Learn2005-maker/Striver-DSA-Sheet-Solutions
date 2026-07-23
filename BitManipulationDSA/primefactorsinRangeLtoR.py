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