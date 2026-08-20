s = "ABAB"
k = 2
n=len(s)
maxlen=0
for i  in range(n):
    uniq=set()
    for j in range(i,n):
        uniq.add(s[j])
        if len(uniq)<=k:
            maxlen=max(maxlen,j-i+1)
        else:
            break
print(maxlen)        

# Time complxity:O(N*N) and s.c:O(1)


s = "ABAB"
k = 2
n=len(s)
maxlen=0
l=0
r=0
dici={}
while r<n:
    dici[s[r]]=dici.get(s[r],0)+1
    while len(dici)>k:
        dici[s[l]]-=1
        if dici[s[l]]==0:
            del dici[s[l]]
        l+=1
    if len(dici)<=k:
        maxlen=max(maxlen,r-l+1)
    r+=1    
print(maxlen)            