def findContentChildren(g,s):
    n=len(g)
    m=len(s)
    g.sort()
    s.sort()
    l=0
    r=0

    while l<m and r<n:
        if s[l]>=g[r]:
            r+=1
        l+=1
    return r

g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))