fruits = [1,2,1]
n=len(fruits)

max_len=0

for i in range(n):
    s=set()
    for j in range(i,n):
        s.add(fruits[j])
        if len(s)<=2:
            max_len=max(max_len,j-i+1)
        else:
            break
            
print(max_len)

# Time complexity:O(n+n)    #    
arr = [1,2,1]
n=len(arr)
max_len=0
l=0
r=0
dici={}
while r<n:
    dici[arr[r]]=dici.get(arr[r],0)+1
    
    while len(dici)>2:
        dici[arr[l]]-=1
        if dici[arr[l]]==0:
            del dici[arr[l]]
        l+=1
    if len(dici)<=2:
        max_len=max(max_len,r-l+1)
    r+=1        
print(max_len)        
        
                