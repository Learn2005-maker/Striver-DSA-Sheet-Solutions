# s = "abcabcbb"
# Brute -Naive Solution
s = "pwwkew"

n=len(s)

max_len=0
for i in range(n):
    dici={}
    for j in range(i,n):
        if s[j] not in dici:
            dici[s[j]]=1
        else:
            break
        max_len=max(max_len,j-i+1)    
print(max_len)        


s = "pwwkew"
n=len(s)
hasTable=set()
max_len=0
l=0
for r in range(n):
    if s[r] in hasTable:
        hasTable.remove(s[l])
        l+=1
    hasTable.add(s[r])    
    max_len=max(max_len,r-l+1)

print(max_len)        








