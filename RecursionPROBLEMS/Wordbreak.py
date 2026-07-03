def wordBreak(start,s,worddict):
    if start==len(s):
        return True
        
    for end in range(start,len(s)):
        substring=s[start:end+1]
        if substring in worddict:
            if wordBreak(end+1,s,worddict):
                return True
    return False            
s = "catsandog"
worddict = ["cats","and","dog","sand","cat"]

res=wordBreak(0,s,set(worddict))
print(res)




