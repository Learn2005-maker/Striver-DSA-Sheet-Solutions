s = "(1+(2*3)+((8)/4))+1"
max_depth=0
cur_depth=0
for ch in s:
    if ch=="(":
        cur_depth+=1
        max_depth=max(max_depth, cur_depth)
    elif ch==")":
        cur_depth-=1

print(max_depth) 
 # Time complexity: O(n) where n is the length of the string
 # Space complexity: O(1) since we are using only a few variables to keep track
 
# Using the Stack approach  
s = "(1+(2*3)+((8)/4))+1"
max_depth=0
stack=[]
for ch in s:
    if ch=="(":
        stack.append(ch)
        max_depth=max(max_depth, len(stack))
    elif ch==")":
        stack.pop()

print(max_depth) 