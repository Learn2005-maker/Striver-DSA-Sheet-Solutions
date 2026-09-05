# our recursive solution has exponential time complexity because every * can create 3 branches.
# If there are k stars:

# Time:  O(3^k)
# Space: O(n)

def checkValidString(s):
    def isValid(index,count):
        # Too many closing brackets
        if count<0:
            return False
        
        if index==len(s):
            if count==0:
                return True
        
        if s[index]=="(":
            return isValid(index+1,count+1)
        if s[index]==")":
            return isValid(index+1,count-1)
        
        return (isValid(index+1,count+1) or isValid(index+1,count)  or isValid(index+1,count-1) )
    return isValid(0,0)  

  
s = "(*))"
  

print(checkValidString(s))



# Time complexcity:O(n) and s.c:O(n)

def checkValidString(s):
    minn=0
    maxx=0

    for i in range(len(s)):
        if s[i]=="(":
            minn+=1
            maxx+=1
        elif s[i]==")":
            minn-=1
            maxx-=1
        else:
            minn-=1
            maxx+=1
        if minn < 0:
            minn=0
        if maxx<0:
            return False
        
    return minn==0

  
s = "***)))***(())"
  

print(checkValidString(s))