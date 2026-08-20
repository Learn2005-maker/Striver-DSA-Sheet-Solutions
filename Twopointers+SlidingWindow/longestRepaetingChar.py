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