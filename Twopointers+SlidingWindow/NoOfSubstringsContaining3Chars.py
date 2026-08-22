s = "aaabbc"

n=len(s)
count=0
for i in range(n):
    dici={'a':0,'b':0,'c':0}
    for j in range(i,n):
        dici[s[j]]=dici.get(s[j],0)+1
        if dici['a']>0 and dici['b']>0 and dici['c']>0:
            count+=(n-j)
            break
print(count)           


# Time complexcity:O(n^2) and S.c:O(3)


def numberOfSubstrings(self, s: str):
    n=len(s)
    count=0
    dici={'a':-1,'b':-1,'c':-1}
    for i in range(n):
        dici[s[i]]=i
        if dici['a']!=-1 and dici['b']!=-1 and dici['c']!=-1:
            count+=min(dici['a'],dici['b'],dici['c'])+1
    
    return  count   



def noofSubstrings(s,n):
    l=0
    n1=len(s)
    r=0
    total=0
    dici={}
    while r<n1:
        dici[s[r]]=dici.get(s[r],0)+1
        while len(dici)>n:
            dici[s[l]]-=1
            if dici[s[l]]==0:
                del dici[s[l]]
            l+=1
        total+=(r-l+1)    
        r+=1
    return total    
    


s = "bbacba"

print(noofSubstrings(s,3)-noofSubstrings(s,2))
# Time complexcity:O(n+n) and S.c:O(1)

# Using the classic sliding window technique of AtMost(K) - AtMost(K-1) 
# To find the number of substrings with exactly K distinct characters.
