# Time complexcity:O(n)
# spac complexcity:O(n)
# Approach: Store opening brackets in Stack.
def isValid(s):
    n=len(s)
    
    stack=[]
    
    for i in range(n):
        if s[i]=='(' or s[i]=='[' or s[i]  =='{':
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            ch=stack[-1]
            stack.pop()
            if s[i]==')' and ch=='(' or s[i]==']' and ch=='[' or s[i]=='}' and ch=='{':
                continue
            else:
                return False
    return len(stack )==0         
            
s="(){}{{{"            
print(isValid(s)   )   



# Time complexcity:O(n)
# Space complexcity:O(n)
# Approach: using map 
def isValid(s):
    stack=[]
    mp={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for ch  in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack and stack[-1]!=mp[ch]:
                return False
            stack.pop()
    return len(stack)==0        
s="(){}{{{"            
print(isValid(s)   )        
        
             
        
        