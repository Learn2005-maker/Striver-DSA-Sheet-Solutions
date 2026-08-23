s1 = "abcdebdde"
s2 = "bde"

n=len(s1)
m=len(s2)

# mpp={}

# for i in s2:
#     mpp[i]=mpp.get(i,0)+1

l=0
r=0
sIndex=-1
minL=float("inf")
while r<n:
    # Step 1: Find s2 as a subsequence
    j=0
    while r<n:
        if s1[r]==s2[j]:
            j+=1
            if j==m:
                break
        r+=1    
    # if subsequence not found 
    if j<m:
        break        
    # Once we find the complete subsequence, we go
    # backwards to find the smallest possible starting position.
    # Step 2: Move backwards to shrink the window
    end=r
    j=m-1
    
    while j>=0:
        if s1[r]==s2[j]:
            j-=1
        r-=1    
    start=r+1    
    # Update minium # 
    if end-start+1<minL:
        minL=end-start+1
        sIndex=start
     # Start searching again after start
    r=start+1
if sIndex==-1:
    print("")
else:
    print(s1[sIndex:sIndex+minL])








