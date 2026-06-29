def isPalindrome(s,start,end):
    while start<=end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True        

def palindromepartition(start,path,ans,s):
    if start==len(s):
        ans.append(path[:])
        return 
    
    for end in range(start,len(s)):
        if isPalindrome(s,start,end):
            path.append(s[start:end+1])
            palindromepartition(end+1,path,ans,s)
            path.pop()
    return ''.join(path)

s="aab"            
ans=[]
palindromepartition(0,[],ans,s)


print(ans)


# Time complexcity:O(2^n)
# Space complexcity:O(n)  if we  exclude the result