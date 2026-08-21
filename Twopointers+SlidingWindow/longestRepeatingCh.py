# T.c:O(n*n)
s = "AABABBA"
k = 1
n=len(s)
maxL=0
for i in range(n):
    dici={}
    maxf=0
    for j in range(i,n):
        ch=s[j]
        dici[ch]=dici.get(ch,0)+1
        maxf=max(maxf,dici[ch])
        changes=(j-i+1)-maxf
        if changes<=k:
            maxL=max(maxL,j-i+1)
        else:
            break
print(maxL)           
            
# T.c:O(n) and S.c:O(26)
s = "AABA"
k = 1

n = len(s)
maxL = 0
l = 0
r = 0
maxf = 0
dici = {}

while r < n:
    ch = s[r]
    dici[ch] = dici.get(ch, 0) + 1

    maxf = max(maxf, dici[ch])

    if (r - l + 1) - maxf > k:
        dici[s[l]] -= 1

        if dici[s[l]] == 0:
            del dici[s[l]]

        l += 1

    maxL = max(maxL, r - l + 1)

    r += 1

print(maxL)
        
        
        
        
            